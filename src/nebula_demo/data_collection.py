import random
import requests
from loguru import logger

def collect_reviews(app_id: str, count: int = 100) -> dict:
    """
    Collects reviews for the specified app using the iTunes RSS feed.
    Downloads 10 pages of reviews and aggregates them.

    Args:
        app_id (str): The app identifier expected by the API.
        count (int): Number of reviews to randomly sample.

    Returns:
        dict: Raw JSON data of reviews, aggregated from 10 pages.
    """
    all_entries = []
    for page in range(1, 11):
        url = f"https://itunes.apple.com/gb/rss/customerreviews/page={page}/id={app_id}/sortBy=mostRecent/json"
        logger.info("Requesting reviews from URL: {}", url)
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            entries = data.get("feed", {}).get("entry", [])
            if entries:
                logger.debug("Found {} entries on page {}.", len(entries), page)
                all_entries.extend(entries)
            else:
                logger.warning("No entries found on page {}.", page)
        except Exception as e:
            logger.error("Error fetching page {} for app_id {}: {}", page, app_id, e)
    if not all_entries:
        logger.warning("No review entries found for app_id: {}", app_id)
        return {}
    # Randomly sample reviews if more than the requested count.
    if len(all_entries) > count:
        logger.debug("Sampling {} out of {} reviews.", count, len(all_entries))
        all_entries = random.sample(all_entries, count)
    logger.success("Successfully collected {} reviews across 10 pages.", len(all_entries))
    return {"feed": {"entry": all_entries}}
