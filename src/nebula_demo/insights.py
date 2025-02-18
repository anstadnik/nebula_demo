import numpy as np
import nltk
import polars as pl
from loguru import logger
from nltk.sentiment import SentimentIntensityAnalyzer
import os

if not os.getenv("RENDER", False):
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

    try:
        topic_model = BERTopic()
    except NameError:
        logger.warning("Topic modeling disabled")
        return [], None

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
    logger.info("Extracting keywords from negative reviews using TF-IDF.")
    negative_df = df.filter(pl.col("sentiment") == "negative")
    negative_texts = negative_df["review_text"].to_list()
    if not negative_texts:
        logger.warning("No negative reviews to extract keywords from.")
        return []

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(negative_texts)
    scores = np.asarray(X.mean(axis=0)).ravel()  # average TF-IDF scores
    indices = scores.argsort()[::-1]
    feature_names = np.array(vectorizer.get_feature_names_out())
    top_keywords = feature_names[indices][:top_n].tolist()
    logger.success("Extracted top {} keywords via TF-IDF.", top_n)
    return top_keywords


def generate_insights(df: pl.DataFrame) -> dict:
    """
    Generates actionable insights by combining sentiment analysis,
    topic grouping for negative reviews, and keyword extraction from both
    TF-IDF and BERTopic's topic info.

    Args:
        df (pl.DataFrame): Processed review data.

    Returns:
        dict: A dictionary containing insights.
    """
    logger.info("Generating insights.")
    df = perform_sentiment_analysis(df)

    # Group negative reviews using BERTopic.
    topics, topic_model = group_negative_reviews(df)

    # Extract keywords from negative reviews using TF-IDF.
    tfidf_keywords = extract_keywords_from_negative_reviews(df)

    # Initialize empty topic info and negative topic keywords.
    topic_info = []
    negative_topic_keywords = []

    if topic_model:
        logger.info("Extracting topic info from BERTopic.")
        # topic_model.get_topic_info returns a pandas DataFrame.
        topic_info_df = topic_model.get_topic_info()
        # Filter out the outlier topic if present (typically labeled as -1).
        topic_info_df = topic_info_df[topic_info_df.Topic != -1]
        topic_info = topic_info_df.to_dict("records")
        # Extract keywords from the "Name" column of the topic info.
        keywords_from_topic = []
        for row in topic_info:
            if "Name" in row and row["Name"]:
                # Assume keywords are comma-separated.
                kws = [kw.strip() for kw in row["Name"].split(",")]
                keywords_from_topic.extend(kws)
        negative_topic_keywords = list(set(keywords_from_topic))
        logger.success(
            "Extracted {} keywords from topic info.", len(negative_topic_keywords)
        )

    sentiment_counts = (
        df.group_by("sentiment")
        .agg(pl.col("sentiment").count().alias("count"))
        .to_dict(as_series=False)
    )
    logger.success("Insights generation complete.")
    return {
        "sentiment_counts": sentiment_counts,
        "negative_review_topics": topics,
        "negative_topic_info": topic_info,
        "negative_review_keywords_tfidf": tfidf_keywords,
        "negative_topic_keywords": negative_topic_keywords,
    }
