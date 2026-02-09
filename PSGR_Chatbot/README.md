# PSGRKCW Smart Assistant Chatbot 🎓

This is a full-stack AI-powered chatbot designed for PSGR Krishnammal College for Women. It uses a Python Flask backend with TF-IDF and NLP intelligence to provide smart responses to queries about admissions, fees, courses, and placements.

## 🚀 Quick Start (Recommended)

Run both the backend and frontend simultaneously from the root directory:

```bash
npm run dev
```

---

## 🏗️ Module-Wise Instructions

### 1. Backend (Python/Flask)
The backend manages the NLP logic and FAQ data.

**Setup:**
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Run:**
```bash
python app.py
```
*Server will run on: http://127.0.0.1:5001*

---

### 2. Frontend (HTML/CSS/JS)
The frontend provides two interfaces for the chatbot.

**Run:**
```bash
cd frontend
npx -y http-server -p 3000
```

**Access Points:**
*   **Modern Chatbot UI:** [http://127.0.0.1:3000/modern_chat.html](http://127.0.0.1:3000/modern_chat.html) (Glassmorphism & Animations)
*   **Standard Chatbot:** [http://127.0.0.1:3000/index.html](http://127.0.0.1:3000/index.html)
*   **Admin Panel:** [http://127.0.0.1:3000/admin.html](http://127.0.0.1:3000/admin.html)

---

## 📂 Project Structure
- `backend/`: Flask API, TF-IDF logic, and FAQ data.
- `frontend/`: Web interface (HTML, CSS, Vanilla JS).
- `package.json`: Contains unified scripts to manage the project.

## ⚙️ Configuration
- **Backend Port:** 5001
- **Frontend Port:** 3000
- **FAQ Data:** `backend/data/faqs_merged.json`
