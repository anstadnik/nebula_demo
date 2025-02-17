# Apple Store Review Analysis API

This project provides an API for collecting, processing, and analyzing Apple Store reviews. It collects 100 random reviews for a specified app, processes the data to extract key fields, calculates metrics, performs sentiment analysis, groups negative reviews using BERTopic, and extracts keywords from negative reviews using TF-IDF. The API also supports visualization endpoints that return images (as base64-encoded PNGs) for charts generated with Altair.

## File Structure

.
├── main.py
├── pyproject.toml
├── README.md
└── src
└── nebula_demo
├── init.py
├── data_collection.py
├── data_processing.py
├── metrics.py
├── insights.py
└── vis.py

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/apple_store_review_analysis.git
   cd apple_store_review_analysis

	2.	Install Dependencies
This project uses Poetry for dependency management. Install Poetry if you haven’t already, then run:

poetry install

Alternatively, you can install dependencies manually using pip:

pip install fastapi uvicorn uvloop requests polars nltk bertopic scikit-learn altair loguru

Note: To generate images from Altair charts, you may need to install additional dependencies (e.g., altair_saver) and ensure that a supported image export method (such as Selenium or VLC) is available.

	3.	Run the API Locally
Start the API with Uvicorn (which uses uvloop for improved performance):

poetry run python main.py

The API will be available at: http://127.0.0.1:8000

API Endpoints
	•	GET /collect?app_id=YOUR_APP_ID
Collects raw review data for the specified app.
	•	GET /metrics?app_id=YOUR_APP_ID
Processes reviews, calculates metrics (average rating, rating distribution, etc.), performs sentiment analysis, and generates insights.
	•	GET /download?app_id=YOUR_APP_ID
Downloads the raw review data as a JSON file.
	•	GET /visualize?app_id=YOUR_APP_ID
Generates and returns visualization images for:
	•	Rating Distribution (bar chart)
	•	Sentiment Distribution (arc chart)
The images are returned as base64-encoded PNG strings that can be rendered in any compatible viewer.

Visualization

The file src/nebula_demo/vis.py contains functions to create Altair charts:
	•	Rating Distribution: A bar chart showing the count of reviews per rating.
	•	Sentiment Distribution: An arc (pie-like) chart showing the percentage of positive, neutral, and negative reviews.

The /visualize endpoint converts these charts to images and returns them as base64-encoded PNGs.

Logging

The API extensively uses loguru for logging. Logs will appear in the console to help trace operations and diagnose issues.

Sample Report

A sample report for a chosen app may include:
	•	Metrics:
	•	Average Rating, Median Rating, Total Reviews
	•	Rating Distribution (e.g., percentage of 5-star, 4-star reviews)
	•	Insights:
	•	Sentiment counts (e.g., 60 positive, 25 neutral, 15 negative)
	•	Grouped topics from negative reviews (using BERTopic)
	•	Top keywords in negative reviews (e.g., “bug”, “crash”, “slow”)

Use the /metrics endpoint to generate these insights and /visualize to obtain the charts for further analysis.

Happy analyzing!

