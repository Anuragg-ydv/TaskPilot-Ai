from flask import Flask, render_template, request
from tools import tools

app = Flask(__name__)

def get_recommendations(user_input):
    user_input = user_input.lower()
    scored = []

    for tool in tools:
        score = 0
        for tag in tool["tags"]:
            if tag in user_input:
                score += 3  # exact tag match = 3 points
        
        if score > 0:
            scored.append({**tool, "score": score})

    # Score ke hisaab se sort, top 5 lo
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:5]

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "")
        results = get_recommendations(query)

    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)