import json
import os
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev_fallback_key")
# Explicitly allow Vercel origin for credentials path
CORS(app, supports_credentials=True, origins=[
    "https://psgrkcw-talk.vercel.app",
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://127.0.0.1:3000",
    "http://localhost:3000"
])

print("--- BACKEND STARTING ---")
# Handle absolute paths for deployment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE = os.path.join(BASE_DIR, "data/faqs_merged.json")

# ---------------- INITIALIZE ENGINES ----------------
def load_faqs():
    try:
        if os.path.exists(FAQ_FILE):
            with open(FAQ_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading FAQs: {e}")
    return []

faqs = load_faqs()

# Precompute TF-IDF
def build_vectorizer():
    global vectorizer, tfidf_matrix, faq_sentences, faqs
    try:
        faq_sentences = [" ".join(f.get("keywords", [])) for f in faqs]
        if not faq_sentences or all(not s.strip() for s in faq_sentences):
            print("No valid FAQ sentences for vectorizer.")
            return None, None
        
        vec = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
        matrix = vec.fit_transform(faq_sentences)
        return vec, matrix
    except Exception as e:
        print(f"Error building vectorizer: {e}")
        return None, None

vectorizer, tfidf_matrix = build_vectorizer()

# ---------------- RELOAD FAQs ----------------
@app.route("/reload-faqs", methods=["POST"])
def reload_faqs():
    """Reload FAQs from file and rebuild vectorizer"""
    global faqs, vectorizer, tfidf_matrix
    faqs = load_faqs()
    vectorizer, tfidf_matrix = build_vectorizer()
    return jsonify({"message": "FAQs reloaded successfully", "total": len(faqs)})

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

# ---------------- IMPORT ADMIN ROUTES ----------------
from admin_routes import init_admin_routes
init_admin_routes(app)
# ---------------- HEALTH CHECK ----------------
@app.route("/health")
def health():
    return {"status": "ok"}

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    print(f"Starting Flask app on port {os.environ.get('PORT', 5001)}")
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
