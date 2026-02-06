# PSGRKCW College Chatbot Project Analysis

## 📌 Project Overview
The **PSGRKCW College Chatbot** is a locally deployed, AI-assisted information system designed for PSGR Krishnammal College for Women. It aims to provide instant responses to queries regarding admissions, courses, fees, placements, and campus facilities.

### Key Objectives
- **Instant Information**: Reduce manual inquiry workload.
- **Domain-Specific**: Organized data for various college departments.
- **Local Deployment**: Runs without needing integration into the main college server.
- **Scalable**: Uses JSON-based knowledge storage for easy updates.

---

## 📂 Project Structure

### 1. Backend (`/backend`)
The backend is built with **Python and Flask**.
- **`app.py`**: The main entry point. Handles `/chat` (POST) and `/admin/add-faq` (POST). Uses a keyword-matching algorithm.
- **`nlp_bert.py`**: An advanced version of the chatbot engine using **Sentence-BERT** (all-MiniLM-L6-v2) for semantic similarity.
- **`nlp_tfidf.py`**: Another NLP variant using **TF-IDF Vectorizer** for text matching.
- **`merge_faqs.py`**: A utility script to consolidate all `faq*.json` files into a single `faqs_merged.json`.
- **`requirements.txt`**: Lists dependencies: `flask`, `flask-cors`, `beautifulsoup4`, `requests`, `scikit-learn`, `sentence-transformers`.

### 2. Knowledge Base (`/backend/data`)
Data is stored in structured **JSON** format.
- **`faqs_merged.json`**: The primary data source containing aggregated FAQs (approx. 40KB).
- **`admissions1.json`, `courses.json`, `fees.json`, `placements.json`**, etc.: Domain-specific datasets.

### 3. Web Scraper (`/backend/scraper`)
Scripts designed to gather data from the college website.
- **`scraper.py`**: Contains fallback FAQ data and saves it to JSON.
- **`faq_scraper.py`, `scrape_admissions.py`, etc.**: Individual scripts for different domains.

### 4. Frontend (`/frontend`)
A clean web interface using **HTML, CSS, and Vanilla JavaScript**.
- **`index.html`**: The main chat interface.
- **`js/chat.js`**: Core logic for sending user messages to the API and displaying bot responses.
- **`admin.html` & `js/admin.js`**: A simple administrative portal for adding new FAQs dynamically.
- **`css/style.css`**: Styling for the chat widget and layout.

### 5. WordPress Theme Component (`/kcw-chatbot-theme-v2`)
A self-contained WordPress theme that includes a built-in chatbot prototype.
- **`index.php`**: Contains a hardcoded FAQ engine in JavaScript. This version is designed for easy integration into the college's main website or a separate WordPress-based portal.
- **`style.css` & `functions.php`**: Standard WordPress theme files for styling and basic functionality.

---

## ⚙️ How It Works

### Standalone Version (Flask + JS)
1. **User Interaction**: The user types a question in the frontend.
2. **API Request**: The frontend sends a POST request with the message to `http://127.0.0.1:5000/chat`.
3. **Keyword Matching**: The Flask backend loads `faqs_merged.json` and checks if any keywords match the user input.
4. **Response Delivery**: If a match is found, the associated reply is returned. Otherwise, a fallback "I didn't understand" message is sent.

### Theme-Integrated Version (PHP + JS)
- Uses a client-side keyword matching system (`faqData` array in `index.php`) for instant, serverless responses within a WordPress environment.

---

## 🔬 Code Analysis & Observations

### Backend Logic (`app.py`)
```python
@app.route("/chat", methods=["POST"])
def chat():
    # ... extraction of user message ...
    faqs = load_faqs()
    for faq in faqs:
        for keyword in faq["keywords"]:
            if keyword.lower() in user_message:
                return jsonify({"reply": faq["reply"]})
    # ... fallback ...
```
- **Strengths**: extremely fast, no complex model loading for basic queries.
- **Weaknesses**: Cannot handle synonyms or typos effectively (unlike the BERT/TF-IDF variants).

### Advanced NLP (`nlp_bert.py`)
- Uses `SentenceTransformer`.
- Provides a **confidence score** and threshold-based responses.
- Significantly better at understanding intent than basic keyword matching.

### Data Management
- The use of `glob.glob("data/faq*.json")` in `merge_faqs.py` makes it easy to add new domain files without changing the merging logic.

---

## 🚀 Potential Enhancements
1. **Frontend-Backend Sync**: The frontend `chat.js` expects `data.domain` and `data.confidence`, but `app.py` doesn't currently provide them. Switching to `nlp_bert.py` logic in `app.py` would fix this.
2. **Database Integration**: While JSON is great for small sets, a real database (SQLite/PostgreSQL) would be better for very large FAQ sets.
3. **UI/UX**: Adding a loading spinner and message timestamps would improve the user experience.
4. **Voice Support**: Mentioned in the documentation as a future goal, could be implemented using Web Speech API.

---

## 📄 Documentation Review
- **`PSGR_Chatbot_Document_Execution_Process.doc.md`**: Provides a very detailed guide on the objective, architecture, and execution steps. It serves as a comprehensive manual for the project.
- **`KCW_Chatbot_Available_Questions_v2.docx.md`**: Lists typical user questions, useful for testing the bot's coverage.
