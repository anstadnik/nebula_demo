import polars as pl
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from bertopic import BERTopic
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download VADER lexicon if not already available.
nltk.download('vader_lexicon', quiet=True)

def perform_sentiment_analysis(df: pl.DataFrame) -> pl.DataFrame:
    """
    Performs sentiment analysis on the review text using NLTK VADER.
    Appends a new column 'sentiment' with values 'positive', 'negative', or 'neutral'.
    
    Args:
        df (pl.DataFrame): Processed review data.
    
    Returns:
        pl.DataFrame: DataFrame with an added 'sentiment' column.
    """
    sia = SentimentIntensityAnalyzer()
    sentiments = []
    for text in df["review_text"]:
        score = sia.polarity_scores(text)
        if score["compound"] >= 0.05:
            sentiment = "positive"
        elif score["compound"] <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        sentiments.append(sentiment)
    # Append sentiment column to the DataFrame
    df = df.with_column(pl.Series(name="sentiment", values=sentiments))
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
    # Filter negative reviews
    negative_df = df.filter(pl.col("sentiment") == "negative")
    negative_texts = negative_df["review_text"].to_list()
    if not negative_texts:
        return [], None
    
    topic_model = BERTopic()
    topics, _ = topic_model.fit_transform(negative_texts)
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
    negative_df = df.filter(pl.col("sentiment") == "negative")
    negative_texts = negative_df["review_text"].to_list()
    if not negative_texts:
        return []
    
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(negative_texts)
    # Compute average TF-IDF score for each term
    scores = np.asarray(X.mean(axis=0)).ravel()
    indices = scores.argsort()[::-1]
    feature_names = np.array(vectorizer.get_feature_names_out())
    top_keywords = feature_names[indices][:top_n].tolist()
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
    # Perform sentiment analysis
    df = perform_sentiment_analysis(df)
    
    # Group negative reviews using BERTopic
    topics, _ = group_negative_reviews(df)
    
    # Extract keywords from negative reviews
    keywords = extract_keywords_from_negative_reviews(df)
    
    # Count sentiments
    sentiment_counts = df.groupby("sentiment").agg(pl.col("sentiment").count().alias("count")).to_dict(as_series=False)
    
    insights_data = {
        "sentiment_counts": sentiment_counts,
        "negative_review_topics": topics,
        "negative_review_keywords": keywords
    }
    return insights_data
