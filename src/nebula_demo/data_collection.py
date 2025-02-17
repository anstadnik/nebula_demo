import random
import requests
from loguru import logger


def collect_reviews(app_id: str, count: int = 100) -> dict:
    """
    Collects reviews for the specified app using the iTunes RSS feed.
    Uses the URL format from the app_review repository as an example.

    Args:
        app_id (str): The app identifier expected by the API.
        count (int): Number of reviews to randomly sample.

    Returns:
        dict: Raw JSON data of reviews.
    """
    url = f"https://itunes.apple.com/gb/rss/customerreviews/page=1/id={app_id}/sortBy=mostRecent/json"
    logger.info("Requesting reviews from URL: {}", url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        entries = data.get("feed", {}).get("entry", [])
        if not entries:
            logger.warning("No review entries found in the response.")
            return {}
        if len(entries) > count:
            logger.debug("Sampling {} out of {} reviews.", count, len(entries))
            entries = random.sample(entries, count)
        data["feed"]["entry"] = entries
        logger.success("Successfully collected {} reviews.", len(entries))
        return data
    except Exception as e:
        logger.error("Error fetching reviews: {}", e)
        return {}
