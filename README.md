# Real-Time-News-Sentiment-Analyzer-Machine-Learning-end-to-end-Project



## 🧠 News Sentiment Analyzer

**News Sentiment Analyzer** is a real-time machine learning web application that fetches live news headlines from a news API, analyzes their sentiment using a fine-tuned transformer model, and displays the results in an interactive dashboard with visualizations. It's designed to help users quickly grasp the tone and emotion of current headlines in an intuitive and visually appealing way.

### 🔥 Key Features

- 📡 **Real-time News Fetching** (no manual refresh needed)
- 💬 **Sentiment Classification** (Positive, Negative, Neutral)
- 📊 **Live Visualizations** (bar charts, sentiment trends)
- 🧠 **Transformer-based Sentiment Analysis**
- 💻 **Streamlit-based UI with progressive loading**
- 🌍 **Filter by Country, Category, and Keyword**

---

## 📸 Demo



https://github.com/user-attachments/assets/d4afa876-b485-45b8-ab2b-96cd8ff6613a



---

## ⚙️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | Streamlit (Python) |
| Backend      | FastAPI |
| ML Model     | HuggingFace Transformers (fine-tuned for sentiment analysis) |
| Data Source  | NewsAPI (or similar news API) |
| Visualizations | Pandas, Streamlit Charts |
| Deployment   | Localhost / Cloud Ready |

---

## 🧪 How It Works

1. **News Fetching**  
   Headlines are pulled live from a news API with filters (country, keyword, category).

2. **Sentiment Inference**  
   Each headline is passed through a transformer model (e.g., BERT) and classified into:
   - `Positive`
   - `Neutral`
   - `Negative`

3. **Streaming UI**  
   The frontend updates headlines incrementally, visualizing sentiment distribution in real-time without needing a page refresh.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bandym05/Real-Time-News-Sentiment-Analyzer-Machine-Learning-end-to-end-Project.git
cd Real-Time-News-Sentiment-Analyzer-Machine-Learning-end-to-end-Project
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

**Frontend Requirements (Streamlit)**
```
streamlit
requests
pandas
```

**Backend Requirements (FastAPI + ML)**
```
fastapi
uvicorn
transformers
torch
newspaper3k
```

### 3. Run the Backend API

```bash
cd backend
uvicorn main:app --reload --port 8000
```

### 4. Run the Streamlit Frontend

```bash
cd frontend
streamlit run streamlit_app.py
```

---

## 🌐 URL Structure

| Action | Route |
|--------|-------|
| Fetch News + Sentiment | `GET /headlines?country=us&category=business&q=bitcoin` |

---

## 📁 Project Structure

```
📦 news-sentiment-analyzer
├── backend
│   ├── main.py              # FastAPI backend serving sentiment-analyzed headlines
│   └── model.py             # ML sentiment classifier logic
├── frontend
│   └── streamlit_app.py     # Streamlit frontend for displaying dashboard
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

---

## 🎯 Future Improvements

- [ ] Live WebSocket updates for ultra-low-latency streaming
- [ ] Historical sentiment trends over time (line chart)
- [ ] Multi-language sentiment support
- [ ] Authenticated user dashboards with saved filters
- [ ] Deploy to Hugging Face Spaces, Streamlit Cloud, or Render

---

## 👨‍💻 Author

**Bandile Malaza**  
📧 [bandymalaza05@gmail.com](mailto:bandymalaza05@gmail.com)  

---

## ⭐️ Show Your Support

If you find this project useful:

🌟 Star the repo  
🔁 Share it  
💬 Give feedback or contribute!
