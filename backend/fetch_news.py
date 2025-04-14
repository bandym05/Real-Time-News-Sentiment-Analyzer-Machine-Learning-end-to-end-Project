# backend/fetch_news.py
import os
import requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "YOUR_NEWS_API_KEY")  # Replace with your actual API key or set as env variable
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def get_headlines(country: str = "us", category: str = None, q: str = None):
    """
    Fetches news headlines based on optional filters.
    Default fetches top headlines for the US.
    """
    params = {
        "apiKey": NEWS_API_KEY,
        "country": country,  # change country code as needed
        "pageSize": 20,      # number of articles
    }
    if category:
        params["category"] = category
    if q:
        params["q"] = q

    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"News API error: {response.status_code} {response.text}")
    
    data = response.json()
    # Return only necessary fields
    headlines = []
    for article in data.get("articles", []):
        headlines.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url")
        })
    return headlines
