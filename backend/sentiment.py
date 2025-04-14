# backend/sentiment.py
from transformers import pipeline

# Initialize the sentiment-analysis pipeline only once when the module loads.
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_text(text: str):
    """
    Returns sentiment analysis for the provided text.
    Output is a list with dict elements, e.g.: [{'label': 'POSITIVE', 'score': 0.99}]
    """
    result = classifier(text)
    return result[0]  # returning first result for simplicity
