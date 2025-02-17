import polars as pl
from loguru import logger


def calculate_metrics(df: pl.DataFrame) -> dict:
    """
    Calculates basic review metrics including:
      - Average rating
      - Median rating
      - Total number of reviews
      - Distribution of ratings (count and percentage)

    Args:
        df (pl.DataFrame): Processed review data.

    Returns:
        dict: Dictionary of calculated metrics.
    """
    logger.info("Calculating metrics.")
    if df.height == 0:
        logger.warning("Empty DataFrame received for metrics calculation.")
        return {}

    avg_rating = df["rating"].mean()
    median_rating = df["rating"].median()
    total_reviews = df.height

    # Group by rating and calculate count and percentage using proper Polars methods.
    dist_df = df.group_by("rating").agg(pl.col("rating").count().alias("count"))
    dist_df = dist_df.with_columns(
        [(pl.col("count") / total_reviews * 100).alias("percentage")]
    )
    rating_distribution = dist_df.to_dict(as_series=False)
    logger.success("Metrics calculation complete.")
    return {
        "average_rating": avg_rating,
        "median_rating": median_rating,
        "total_reviews": total_reviews,
        "rating_distribution": rating_distribution,
    }
