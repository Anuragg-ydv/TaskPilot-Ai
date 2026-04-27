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
| Recommendation Logic | Rule-based keyword matching |
| Data Store | `tools.py` (hardcoded tool database) |

---

## Project Structure

```
TaskPilot AI/
├── app.py              # Flask app + recommendation logic
├── tools.py            # AI tools database
├── utils.py            # Helper functions
├── requirements.txt    # Dependencies
├── README.md           # This file
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
get_recommendations() runs
        ↓
Each tool's tags matched against user input
        ↓
Score calculated — more matches = higher score
        ↓
Top 5 tools sorted by score
        ↓
Jinja2 renders results on screen
```

Each tool in the database has a set of `tags`. When a user types something, the engine checks how many tags match the input. The more matches, the higher the tool ranks.

```python
# Core logic — as simple as this
for tag in tool["tags"]:
    if tag in user_input:
        score += 3
```

---

## Is This Actually AI?

**Honest answer — not yet.**

Currently TaskPilot AI is a **rule-based recommendation system**. It uses keyword matching, not machine learning. It will not understand `"kuch visual banana hai"` the same way a true AI would understand `"image banana hai"`.

This is intentional — the goal was to build a clean, working foundation first.

---

## Roadmap — Becoming Fully AI

```
Current   →   Rule-based keyword matching        ✅ Done
              Fast, accurate, working

Stage 2   →   TF-IDF + Cosine Similarity          🔜 Next
              Will understand meaning, not just keywords
              "visual banana" will match image tools too

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
Roll No: 24f3004822

---

## License

MIT License — free to use, modify, and distribute.

---

> *"This project is not a destination — it's a starting point. As I learn ML, this app will grow with me."*