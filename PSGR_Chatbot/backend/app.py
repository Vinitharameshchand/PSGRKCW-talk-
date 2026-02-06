import json
import os
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

FAQ_FILE = "data/faqs_merged.json"

# ---------------- INITIALIZE ENGINES ----------------
def load_faqs():
    if os.path.exists(FAQ_FILE):
        with open(FAQ_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

faqs = load_faqs()

# Precompute TF-IDF
def build_vectorizer():
    global vectorizer, tfidf_matrix, faq_sentences, faqs
    faq_sentences = [" ".join(f["keywords"]) for f in faqs]
    if not faq_sentences:
        return None, None
    
    vec = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
    matrix = vec.fit_transform(faq_sentences)
    return vec, matrix

vectorizer, tfidf_matrix = build_vectorizer()

# ---------------- HOME ----------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask server is running with TF-IDF intelligence"})

# ---------------- CHAT API ----------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"reply": "Please type a question."}), 400

    user_message = data["message"].lower().strip()

    # 1. Try Simple Keyword Matching (Fast & exact)
    for faq in faqs:
        for keyword in faq["keywords"]:
            if keyword.lower() in user_message:
                return jsonify({
                    "reply": faq["reply"],
                    "method": "keyword",
                    "domain": faq.get("domain", "general")
                })

    # 2. Try TF-IDF Similarity (Statistical Fallback)
    if vectorizer and tfidf_matrix is not None:
        user_vec = vectorizer.transform([user_message])
        similarities = cosine_similarity(user_vec, tfidf_matrix)[0]
        best_idx = np.argmax(similarities)
        confidence = float(similarities[best_idx])

        if confidence > 0.2:  # TF-IDF confidence threshold is lower than BERT
            return jsonify({
                "reply": faqs[best_idx]["reply"],
                "method": "tfidf",
                "confidence": round(confidence, 2),
                "domain": faqs[best_idx].get("domain", "general")
            })

    return jsonify({
        "reply": "Sorry, I didn't understand that. Could you try rephrasing? You can ask about admissions, courses, fees, or placements.",
        "method": "none"
    })

# ---------------- ADMIN ADD FAQ ----------------
@app.route("/admin/add-faq", methods=["POST"])
def add_faq():
    global faqs, vectorizer, tfidf_matrix
    data = request.get_json()

    domain = data.get("domain")
    keywords = data.get("keywords")
    reply = data.get("reply")

    if not domain or not keywords or not reply:
        return jsonify({"error": "All fields are required"}), 400

    faqs.append({
        "domain": domain,
        "keywords": [k.strip().lower() for k in keywords],
        "reply": reply
    })

    with open(FAQ_FILE, "w", encoding="utf-8") as f:
        json.dump(faqs, f, indent=4, ensure_ascii=False)

    # Rebuild vectorizer
    vectorizer, tfidf_matrix = build_vectorizer()

    return jsonify({"message": "FAQ added successfully"})

if __name__ == "__main__":
    app.run(port=5001, debug=True, use_reloader=False)
