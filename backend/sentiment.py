# backend/sentiment.py
from transformers import pipeline

label_map = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def analyze_text(text: str):
    result = classifier(text)[0]
    label = label_map.get(result["label"], "Unknown")
    return {"label": label, "score": round(result["score"], 2)}
