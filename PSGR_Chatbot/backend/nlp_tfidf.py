import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FAQ_FILE = "data/faqs_updated.json"

vectorizer = None
tfidf_matrix = None
questions = []
faqs = []


def load_faqs():
    global vectorizer, tfidf_matrix, questions, faqs

    with open(FAQ_FILE, "r", encoding="utf-8") as f:
        faqs = json.load(f)

    questions = []
    for faq in faqs:
        questions.extend(faq["keywords"])

    if not questions:
        return

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions)


def reload_faqs():
    load_faqs()


def get_tfidf_response(user_query):
    global vectorizer, tfidf_matrix, questions, faqs

    if vectorizer is None or tfidf_matrix is None:
        load_faqs()

    query_vec = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix)[0]

    best_idx = similarities.argmax()
    confidence = float(similarities[best_idx])

    if confidence < 0.2:
        return {
            "reply": "Sorry, I couldn't find an exact answer.",
            "confidence": 0.0,
            "domain": "unknown"
        }

    keyword = questions[best_idx]

    for faq in faqs:
        if keyword in faq["keywords"]:
            return {
                "reply": faq["reply"],
                "confidence": round(confidence, 2),
                "domain": faq.get("domain", "general")
            }

    return {
        "reply": "Sorry, no matching answer found.",
        "confidence": 0.0,
        "domain": "unknown"
    }
