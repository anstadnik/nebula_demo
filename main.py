import json
import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn

# Import functions from the src package
from src.nebula_demo import data_collection, data_processing, metrics, insights

app = FastAPI(
    title="Apple Store Review Analysis API",
    description="API to collect and analyze Apple Store reviews.",
    version="0.1.0"
)

@app.get("/collect")
async def collect_reviews_endpoint(app_id: str):
    """
    Endpoint to collect raw reviews for a specified app.
    """
    raw_data = data_collection.collect_reviews(app_id)
    if not raw_data:
        raise HTTPException(status_code=404, detail="No data found for the given app_id")
    # Optionally, save raw data to a file for download
    with open("raw_reviews.json", "w") as f:
        json.dump(raw_data, f)
    return raw_data

@app.get("/metrics")
async def metrics_endpoint(app_id: str):
    """
    Endpoint to process reviews, calculate metrics, and generate insights.
    """
    raw_data = data_collection.collect_reviews(app_id)
    if not raw_data:
        raise HTTPException(status_code=404, detail="No data found for the given app_id")
    
    df = data_processing.process_reviews(raw_data)
    if df.is_empty():
        raise HTTPException(status_code=404, detail="No reviews processed from raw data")
    
    met = metrics.calculate_metrics(df)
    insights_data = insights.generate_insights(df)
    
    return {"metrics": met, "insights": insights_data}

@app.get("/download")
async def download_raw_reviews(app_id: str):
    """
    Endpoint to download raw review data as a JSON file.
    """
    raw_data = data_collection.collect_reviews(app_id)
    if not raw_data:
        raise HTTPException(status_code=404, detail="No data found for the given app_id")
    
    filename = f"{app_id}_raw_reviews.json"
    with open(filename, "w") as f:
        json.dump(raw_data, f)
    
    # Ensure file exists before returning
    if os.path.exists(filename):
        return FileResponse(filename, media_type='application/json', filename=filename)
    else:
        raise HTTPException(status_code=500, detail="File could not be created.")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
