# frontend/streamlit_app.py
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- CONFIGURATION ---
API_URL = "http://localhost:8000/headlines"

# --- SIDEBAR FILTERS ---
st.sidebar.title("Filters")
country = st.sidebar.text_input("Country Code", value="us", help="Enter a 2-letter country code, e.g., us")
category = st.sidebar.text_input("Category", value="", help="Enter category (business, technology, etc.)")
keyword = st.sidebar.text_input("Keyword", value="", help="Search news by keyword")

# --- FETCH DATA FROM API ---
params = {"country": country}
if category:
    params["category"] = category
if keyword:
    params["q"] = keyword

try:
    response = requests.get(API_URL, params=params)
    data = response.json()
    articles = data.get("articles", [])
    last_updated = datetime.now().strftime("%d %B %Y at %I:%M%p").lower().replace('am', 'am').replace('pm', 'pm')
except Exception as e:
    st.error(f"Error fetching data: {e}")
    articles = []
    last_updated = None

# --- DISPLAY DATA ---
st.title("🧠 News Sentiment Analyzer Dashboard")

if articles:
    # Create a DataFrame for easier manipulation
    df = pd.DataFrame(articles)

    # Show a table of headlines and sentiments
    st.subheader("📋 Headlines & Sentiments")
    st.write("Live headlines fetched from News API with sentiment analysis results:")
    st.markdown(f"<hr/><p style='text-align: right; color: gray;'>Last updated: <b>{last_updated}</b></p>", unsafe_allow_html=True)

    df_display = df[["title", "sentiment"]].copy()
    df_display["sentiment_label"] = df_display["sentiment"].apply(lambda x: x.get("label"))
    df_display["sentiment_score"] = df_display["sentiment"].apply(lambda x: round(x.get("score", 0), 2))

    st.dataframe(df_display[["title", "sentiment_label", "sentiment_score"]], height=400)

    # Plot sentiment distribution
    st.subheader("📊 Sentiment Distribution")
    sentiment_counts = df_display["sentiment_label"].value_counts()
    st.bar_chart(sentiment_counts)

    # Show article details
    st.subheader("📰 Article Details")
    article_index = st.selectbox("Select an article", df.index, format_func=lambda i: df.at[i, "title"])
    if article_index is not None:
        st.markdown(f"**Title:** {df.at[article_index, 'title']}")
        st.markdown(f"**Description:** {df.at[article_index, 'description']}")
        st.markdown(f"[Read full article]({df.at[article_index, 'url']})")

    # --- LAST UPDATED FOOTER ---
    if last_updated:
        st.markdown(f"<hr/><p style='text-align: right; color: gray;'>Last updated: <b>{last_updated}</b></p>", unsafe_allow_html=True)
else:
    st.info("No articles found. Adjust filters and try again.")
