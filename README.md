# PSGRKCW Project Overview & Deployment Guide 🚀

This repository contains the complete source code for the PSGR Krishnammal College for Women project, including the Smart Assistant Chatbot, a WordPress theme, and a landing page prototype.

## 📂 Project Structure

The project is organized into three main components:

```
/Users/vinitha/PSGRKCW-talk-/
├── PSGR_Chatbot/               # 🤖 MAIN APPLICATION (Flask + JS)
│   ├── backend/                # Python Flask API & NLP Logic
│   │   ├── app.py              # Entry point
│   │   ├── requirements.txt    # Python dependencies
│   │   └── data/               # FAQ knowledge base
│   ├── frontend/               # User Interface (HTML/CSS/JS)
│   │   ├── index.html          # Standard Chat
│   │   ├── modern_chat.html    # Modern UI
│   │   └── admin.html          # Admin Panel
│   └── package.json            # Orchestration scripts
│
├── kcw-chatbot-theme-v2/       # 🎨 WORDPRESS THEME
│   ├── index.php               # Theme template
│   ├── style.css               # Theme styles
│   └── functions.php           # Theme logic
│
└── sample_landing_page/        # 📄 LANDING PAGE PROTOTYPE
    ├── index.html              # Landing page structure
    └── css/, js/               # Assets
```

---

## 🚀 Deployment Instructions

### 1. PSGR Chatbot (Main Application)

This is a full-stack application requiring a Python backend and a static frontend server.

#### Prerequisites
- **Python 3.8+**
- **Node.js & npm**

#### Step-by-Step Deployment

1.  **Backend Setup**:
    ```bash
    cd PSGR_Chatbot/backend
    python3 -m venv venv        # Create virtual environment
    source venv/bin/activate    # Activate (Windows: venv\Scripts\activate)
    pip install -r requirements.txt
    ```

2.  **Run the Application** (from `PSGR_Chatbot` root):
    You can run both backend and frontend with a single command:
    ```bash
    cd PSGR_Chatbot
    npm install                 # Install dependencies
    npm run dev                 # Starts Backend (5001) & Frontend (3000)
    ```

3.  **Access Points**:
    -   **Modern Chat**: [http://localhost:3000/modern_chat.html](http://localhost:3000/modern_chat.html)
    -   **Admin Panel**: [http://localhost:3000/admin.html](http://localhost:3000/admin.html)
    -   **API Endpoint**: [http://localhost:5001](http://localhost:5001)

---

### 2. WordPress Theme (`kcw-chatbot-theme-v2`)

This custom theme integrates the chatbot into a WordPress site.

#### Installation
1.  **Zip the Folder**:
    Compress the `kcw-chatbot-theme-v2` folder into a `.zip` file.
2.  **Upload to WordPress**:
    -   Go to WP Admin > **Appearance** > **Themes**.
    -   Click **Add New** > **Upload Theme**.
    -   Select your zip file and install.
3.  **Activate**:
    -   Click **Activate** after installation.

---

### 3. Sample Landing Page (`sample_landing_page`)

A standalone landing page prototype for the college talk.

#### Deployment
This is a static HTML site. You can deploy it using any static hosting service (GitHub Pages, Netlify, Vercel) or a simple web server.

**Local Run**:
```bash
cd sample_landing_page
npx http-server -p 8080
```
Then access at [http://localhost:8080](http://localhost:8080).

---

## 🛠 Troubleshooting

-   **Backend Protocol Errors**: Ensure `app.py` is running on port 5001. Check `backend` terminal for errors.
-   **CORS Issues**: The Flask app is configured with `flask-cors` to allow requests from the frontend. Ensure you are accessing via `localhost`.
-   **Missing Dependencies**: Always run `pip install -r requirements.txt` in the backend folder and `npm install` in the `PSGR_Chatbot` folder before starting.
