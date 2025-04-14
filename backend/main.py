# backend/main.py
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.fetch_news import get_headlines
from backend.sentiment import analyze_text

app = FastAPI(title="News Sentiment Analyzer API")

# Allow CORS for local development with Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/headlines")
def fetch_headlines(
    country: str = Query("us", description="Country code (e.g., 'us', 'gb', etc.)"),
    category: str = Query(None, description="News category (e.g., business, technology)"),
    q: str = Query(None, description="Keyword to search for")
):
    try:
        headlines = get_headlines(country, category, q)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # Process each headline with sentiment analysis
    results = []
    for article in headlines:
        title = article.get("title")
        sentiment = analyze_text(title) if title else {"label": "UNKNOWN", "score": 0.0}
        results.append({
            "title": title,
            "description": article.get("description"),
            "url": article.get("url"),
            "sentiment": sentiment
        })
    return {"articles": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
