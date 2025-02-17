import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from loguru import logger
import uvicorn


# Import functions from our src package.
from src.nebula_demo import data_collection, data_processing, metrics, insights, vis

app = FastAPI(
    title="Apple Store Review Analysis API",
    description="API to collect and analyze Apple Store reviews.",
    version="0.1.0",
)


@app.get("/collect")
async def collect_reviews_endpoint(app_id: str):
    """
    Endpoint to collect raw reviews for a specified app.
    """
    logger.info("Endpoint /collect called with app_id: {}", app_id)
    raw_data = data_collection.collect_reviews(app_id)
    if not raw_data:
        logger.error("No data found for app_id: {}", app_id)
        raise HTTPException(
            status_code=404, detail="No data found for the given app_id"
        )
    filename = "raw_reviews.json"
    with open(filename, "w") as f:
        json.dump(raw_data, f)
    logger.success("Raw data collected and saved to {}.", filename)
    return raw_data


@app.get("/metrics")
async def metrics_endpoint(app_id: str):
    """
    Endpoint to process reviews, calculate metrics, and generate insights.
    """
    logger.info("Endpoint /metrics called with app_id: {}", app_id)
    raw_data = data_collection.collect_reviews(app_id)
    if not raw_data:
        logger.error("No data found for app_id: {}", app_id)
        raise HTTPException(
            status_code=404, detail="No data found for the given app_id"
        )
    df = data_processing.process_reviews(raw_data)
    if df.height == 0:
        logger.error("No reviews processed from raw data for app_id: {}", app_id)
        raise HTTPException(
            status_code=404, detail="No reviews processed from raw data"
        )
    met = metrics.calculate_metrics(df)
    insights_data = insights.generate_insights(df)
    logger.success("Metrics and insights generated for app_id: {}", app_id)
    return {"metrics": met, "insights": insights_data}


@app.get("/download")
async def download_raw_reviews(app_id: str):
    """
    Endpoint to download raw review data as a JSON file.
    """
    logger.info("Endpoint /download called with app_id: {}", app_id)
    raw_data = data_collection.collect_reviews(app_id)
    if not raw_data:
        logger.error("No data found for app_id: {}", app_id)
        raise HTTPException(
            status_code=404, detail="No data found for the given app_id"
        )
    filename = f"{app_id}_raw_reviews.json"
    with open(filename, "w") as f:
        json.dump(raw_data, f)
    if os.path.exists(filename):
        logger.success("File {} created for download.", filename)
        return FileResponse(filename, media_type="application/json", filename=filename)
    else:
        logger.error("File {} could not be created.", filename)
        raise HTTPException(status_code=500, detail="File could not be created.")


@app.get("/visualize")
async def visualize_endpoint(app_id: str):
    """
    Endpoint to generate and return visualization images for the review data.
    Returns base64-encoded PNG images for:
      - Rating Distribution (bar chart)
      - Sentiment Distribution (arc chart)
    """
    logger.info("Endpoint /visualize called with app_id: {}", app_id)
    raw_data = data_collection.collect_reviews(app_id)
    if not raw_data:
        logger.error("No data found for app_id: {}", app_id)
        raise HTTPException(
            status_code=404, detail="No data found for the given app_id"
        )
    df = data_processing.process_reviews(raw_data)
    if df.height == 0:
        logger.error("No reviews processed for app_id: {}", app_id)
        raise HTTPException(
            status_code=404, detail="No reviews processed from raw data"
        )
    # Ensure sentiment analysis is performed for the sentiment chart.
    df = insights.perform_sentiment_analysis(df)
    rating_chart = vis.plot_rating_distribution(df)
    sentiment_chart = vis.plot_sentiment_distribution(df)
    logger.success("Visualization specs generated for app_id: {}", app_id)
    return JSONResponse(
        {
            "rating_chart": rating_chart.to_url(),
            "sentiment_chart": sentiment_chart.to_url(),
        }
    )


if __name__ == "__main__":
    logger.info("Starting API server on http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
