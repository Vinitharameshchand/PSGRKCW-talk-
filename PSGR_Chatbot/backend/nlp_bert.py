import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/faqs_merged.json", "r", encoding="utf-8") as f:
    faqs = json.load(f)

sentences = [" ".join(faq["keywords"]) for faq in faqs]
embeddings = model.encode(sentences)

def get_bert_response(user_input):
    user_embedding = model.encode([user_input])
    similarity = cosine_similarity(user_embedding, embeddings)[0]

    best_idx = np.argmax(similarity)
    confidence = similarity[best_idx]

    if confidence < 0.35:
        return {
            "reply": "Sorry, I couldn't find a relevant answer.",
            "confidence": round(float(confidence), 2),
            "domain": "unknown"
        }

    return {
        "reply": faqs[best_idx]["reply"],
        "confidence": round(float(confidence), 2),
        "domain": faqs[best_idx]["domain"]
    }
