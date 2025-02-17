import requests
import random

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
    # Example URL (this is based on the sample JSON structure provided)
    url = f"https://itunes.apple.com/gb/rss/customerreviews/page=1/id={app_id}/sortBy=mostRecent/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract reviews list from the JSON structure
        entries = data.get("feed", {}).get("entry", [])
        if not entries:
            return {}
        
        # Randomly sample reviews if more than the requested count
        if len(entries) > count:
            entries = random.sample(entries, count)
        data["feed"]["entry"] = entries
        
        return data
    except Exception as e:
        print(f"Error fetching reviews: {e}")
        return {}
