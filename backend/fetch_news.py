# backend/fetch_news.py
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_headlines(country: str = "us", category: str = None, q: str = None):
    """
    Fetches news headlines from NewsAPI based on optional filters.
    """
    if not NEWS_API_KEY:
        raise EnvironmentError("Missing NEWS_API_KEY in environment variables")

    params = {
        "apiKey": NEWS_API_KEY,
        "country": country,
        "pageSize": 20,
    }
    if category:
        params["category"] = category
    if q:
        params["q"] = q

    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"News API error: {response.status_code} {response.text}")
    
    data = response.json()
    headlines = []
    for article in data.get("articles", []):
        headlines.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url")
        })
    return headlines
