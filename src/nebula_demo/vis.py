import altair as alt
import polars as pl

def plot_rating_distribution(df: pl.DataFrame) -> alt.Chart:
    """
    Creates an Altair bar chart visualizing the rating distribution.
    
    Args:
        df (pl.DataFrame): Processed review data.
        
    Returns:
        alt.Chart: Altair chart object.
    """
    # Group data by rating
    dist_df = df.groupby("rating").agg(pl.col("rating").count().alias("count")).to_pandas()
    
    chart = alt.Chart(dist_df).mark_bar().encode(
        x=alt.X('rating:O', title='Rating'),
        y=alt.Y('count:Q', title='Count'),
        tooltip=['rating', 'count']
    ).properties(
        title="Rating Distribution"
    )
    return chart

def plot_sentiment_distribution(df: pl.DataFrame) -> alt.Chart:
    """
    Creates an Altair pie chart visualizing the sentiment distribution.
    Note: Altair does not have a native pie chart so we use a workaround with bar charts.
    
    Args:
        df (pl.DataFrame): DataFrame that includes a 'sentiment' column.
        
    Returns:
        alt.Chart: Altair chart object.
    """
    # Count sentiment values
    sentiment_df = df.groupby("sentiment").agg(pl.col("sentiment").count().alias("count")).to_pandas()
    sentiment_df['percentage'] = sentiment_df['count'] / sentiment_df['count'].sum() * 100

    chart = alt.Chart(sentiment_df).mark_arc().encode(
        theta=alt.Theta(field="count", type="quantitative", title="Count"),
        color=alt.Color(field="sentiment", type="nominal", title="Sentiment"),
        tooltip=['sentiment', 'count', alt.Tooltip('percentage', format='.1f')]
    ).properties(
        title="Sentiment Distribution"
    )
    return chart
