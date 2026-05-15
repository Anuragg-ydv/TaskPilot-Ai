import os

from flask import Flask, render_template, request
from tools import tools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# ── ML MODEL — app start pe ek baar train hoga ──
tool_sentences = [
    f"{t['name']} {t['desc']} {' '.join(t['tags'])}"
    for t in tools
]

vectorizer = TfidfVectorizer()
tool_vectors = vectorizer.fit_transform(tool_sentences)

# ── RECOMMENDATION FUNCTION ───────────────────
def get_recommendations(user_input):
    user_vector = vectorizer.transform([user_input])
    scores = cosine_similarity(user_vector, tool_vectors)[0]

    results = []
    for i, score in enumerate(scores):
        if score > 0.05:
            results.append({**tools[i], "score": round(float(score), 2)})

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:5]

# ── ROUTES — Same as before ───────────────────
@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query", "")
        results = get_recommendations(query)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))