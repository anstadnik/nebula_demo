import polars as pl

def process_reviews(raw_data: dict) -> pl.DataFrame:
    """
    Converts raw JSON review data to a Polars DataFrame and processes it.
    Extracts key fields and performs basic text cleaning.
    
    Args:
        raw_data (dict): The raw JSON review data.
        
    Returns:
        pl.DataFrame: Processed review data.
    """
    entries = raw_data.get("feed", {}).get("entry", [])
    if not entries:
        return pl.DataFrame()
    
    records = []
    for entry in entries:
        review_text = entry.get("content", {}).get("label", "")
        rating = int(entry.get("im:rating", {}).get("label", 0))
        title = entry.get("title", {}).get("label", "")
        records.append({
            "review_text": review_text,
            "rating": rating,
            "title": title
        })
    
    df = pl.DataFrame(records)
    # Basic cleaning: convert text to lowercase
    df = df.with_columns([
        pl.col("review_text").str.to_lowercase().alias("review_text"),
        pl.col("title").str.to_lowercase().alias("title")
    ])
    return df
