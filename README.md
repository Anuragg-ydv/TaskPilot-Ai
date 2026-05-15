# TaskPilot AI 🤖

> Apna kaam likho — sahi AI tool khud aa jayega.

A rule-based AI tool recommendation system built with Python and Flask. Describe your task in simple words and TaskPilot AI suggests the best AI tools for that job — no confusion, no endless Googling.

---

## What It Does

Got a task but don't know which AI tool to use? Just type it in — TaskPilot AI matches your input against a curated database of AI tools and returns the top 5 most relevant ones instantly.

**Examples:**
- Type `logo banana hai` → Midjourney, Adobe Firefly, DALL·E
- Type `code debug karna hai` → GitHub Copilot, Cursor
- Type `gaana banana hai` → Suno AI, Udio

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.x + Flask |
| Frontend | HTML + Bootstrap 5 + Jinja2 |
| Recommendation Logic | TF-IDF Vectorization + Cosine Similarity (Machine Learning) |
| Data Store | `tools.py` (hardcoded tool database) |

---

## Project Structure

```
TaskPilot AI/
├── app.py              # Flask app + recommendation logic
├── tools.py            # AI tools database
├── requirements.txt    # Dependencies
├── README.md           # This file
├── practice code/      # Practice and experimental code
├── static/             # Static assets (CSS, JS, images)
└── templates/
    └── index.html      # Frontend UI
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/taskpilot-ai.git
cd taskpilot-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## How It Works

```
User types a task
        ↓
Flask receives POST request
        ↓
TF-IDF vectorization on user input
        ↓
Cosine similarity with all tool vectors
        ↓
Top 5 tools sorted by similarity score
        ↓
Jinja2 renders results on screen
```

The system creates a "sentence" for each tool combining name, description, and tags. It then vectorizes these sentences and the user query using TF-IDF, which gives higher weight to rare but important words. Cosine similarity measures how close the query vector is to each tool vector.

```python
# ML-powered recommendation
tool_sentences = [f"{t['name']} {t['desc']} {' '.join(t['tags'])}" for t in tools]
vectorizer = TfidfVectorizer()
tool_vectors = vectorizer.fit_transform(tool_sentences)
user_vector = vectorizer.transform([user_input])
scores = cosine_similarity(user_vector, tool_vectors)[0]
results = sorted(zip(tools, scores), key=lambda x: x[1], reverse=True)[:5]
```

---

## Is This Actually AI?

**Yes!** TaskPilot AI now uses **machine learning** for recommendations.

It employs **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization to convert tool descriptions and tags into numerical vectors, then uses **cosine similarity** to find the most relevant tools for user queries.

This allows semantic understanding — "visual banana" will match image tools even if exact keywords don't match.

```python
# Core ML logic
tool_sentences = [f"{t['name']} {t['desc']} {' '.join(t['tags'])}" for t in tools]
vectorizer = TfidfVectorizer()
tool_vectors = vectorizer.fit_transform(tool_sentences)
user_vector = vectorizer.transform([user_input])
scores = cosine_similarity(user_vector, tool_vectors)[0]
```

---

## Roadmap — Becoming Fully AI

```
Current   →   TF-IDF + Cosine Similarity          ✅ Done
              Semantic understanding, not just keywords
              "visual banana" matches image tools

Stage 2   →   Fine-tuned Transformer Model       🔜 Next
              Better semantic matching, Hindi support
              Custom embeddings for AI tools domain

Stage 3   →   OpenAI API integration              📅 Planned
              Real language understanding
              Full Hindi language support

Stage 4   →   Custom trained ML model             🎯 Final Goal
              No external API dependency
              Fully personalized recommendations
```

---

## Requirements

```
flask
scikit-learn
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Contributing

Pull requests are welcome. If you'd like to add more tools to the database, edit `tools.py` — each tool follows this structure:

```python
{
    "name": "Tool Name",
    "desc": "What this tool does",
    "link": "https://tool-website.com",
    "tags": ["keyword1", "keyword2", "keyword3"]
}
```

---

## Author

**Anurag Yadav**
BS in Data Science and Applications — IIT Madras


---

## License

## License

Copyright (c) 2025 Anurag Yadav. All Rights Reserved.
This project may not be copied, modified, or distributed without prior written permission from the author.
---

> *"This project is not a destination — it's a starting point. As I learn ML, this app will grow with me."*