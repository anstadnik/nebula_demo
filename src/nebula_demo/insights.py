import numpy as np
import nltk
import polars as pl
from loguru import logger
from nltk.sentiment import SentimentIntensityAnalyzer
from bertopic import BERTopic
from sklearn.feature_extraction.text import TfidfVectorizer

# Download the VADER lexicon if not already present.
nltk.download("vader_lexicon", quiet=True)


def perform_sentiment_analysis(df: pl.DataFrame) -> pl.DataFrame:
    """
    Performs sentiment analysis on the review text using NLTK VADER.
    Appends a new column 'sentiment' with values 'positive', 'negative', or 'neutral'.

    Args:
        df (pl.DataFrame): Processed review data.

    Returns:
        pl.DataFrame: DataFrame with an added 'sentiment' column.
    """
    logger.info("Starting sentiment analysis.")
    sia = SentimentIntensityAnalyzer()
    sentiments = []
    for text in df["review_text"]:
        score = sia.polarity_scores(text)
        if score["compound"] >= 0.05:
            sentiments.append("positive")
        elif score["compound"] <= -0.05:
            sentiments.append("negative")
        else:
            sentiments.append("neutral")
    df = df.with_columns([pl.Series(name="sentiment", values=sentiments)])
    logger.success("Sentiment analysis complete.")
    return df


def group_negative_reviews(df: pl.DataFrame):
    """
    Groups negative reviews using BERTopic.

    Args:
        df (pl.DataFrame): DataFrame containing a 'sentiment' column.

    Returns:
        tuple: (topics, topic_model) where topics is a list of topic assignments
               for negative reviews and topic_model is the fitted BERTopic model.
    """
    logger.info("Grouping negative reviews with BERTopic.")
    negative_df = df.filter(pl.col("sentiment") == "negative")
    negative_texts = negative_df["review_text"].to_list()
    if not negative_texts:
        logger.warning("No negative reviews found for topic modeling.")
        return [], None

    topic_model = BERTopic()
    topics, _ = topic_model.fit_transform(negative_texts)
    logger.success("Negative reviews grouped into {} topics.", len(set(topics)))
    return topics, topic_model


def extract_keywords_from_negative_reviews(df: pl.DataFrame, top_n: int = 10) -> list:
    """
    Uses TF-IDF to extract common keywords from negative reviews.

    Args:
        df (pl.DataFrame): DataFrame containing a 'sentiment' column.
        top_n (int): Number of top keywords to extract.

    Returns:
        list: List of top keywords.
    """
    logger.info("Extracting keywords from negative reviews.")
    negative_df = df.filter(pl.col("sentiment") == "negative")
    negative_texts: list[str] = negative_df["review_text"].to_list()
    if not negative_texts:
        logger.warning("No negative reviews to extract keywords from.")
        return []

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(negative_texts)
    scores = np.asarray(X.mean(axis=0)).ravel()  # average TF-IDF scores
    indices = scores.argsort()[::-1]
    feature_names = np.array(vectorizer.get_feature_names_out())
    top_keywords = feature_names[indices][:top_n].tolist()
    logger.success("Extracted top {} keywords.", top_n)
    return top_keywords


def generate_insights(df: pl.DataFrame) -> dict:
    """
    Generates actionable insights by combining sentiment analysis,
    topic grouping for negative reviews, and keyword extraction.

    Args:
        df (pl.DataFrame): Processed review data.

    Returns:
        dict: A dictionary containing insights.
    """
    logger.info("Generating insights.")
    df = perform_sentiment_analysis(df)
    topics, topic_model = group_negative_reviews(df)
    keywords = extract_keywords_from_negative_reviews(df)
    sentiment_counts = (
        df.group_by("sentiment")
        .agg(pl.col("sentiment").count().alias("count"))
        .to_dict(as_series=False)
    )
    logger.success("Insights generation complete.")
    return {
        "sentiment_counts": sentiment_counts,
        "negative_review_topics": topics,
        "negative_review_keywords": keywords,
    }
