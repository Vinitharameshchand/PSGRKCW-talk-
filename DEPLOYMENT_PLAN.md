# Professional Deployment Plan: PSGRKCW Chatbot

This plan outlines the two-phase deployment process to take your project from your local computer to the live internet. We will use **Render** for the "brain" (Backend) and **Vercel** for the "face" (Landing Page).

## Phase 1: Deploying the Backend (Render.com)

This connects your Flask server to a live URL.

### 1. Account Setup
1. Log in to [dashboard.render.com](https://dashboard.render.com).
2. Click **New +** > **Web Service**.
3. Connect your GitHub repository: `PSGRKCW-talk-`.

### 2. Configuration Settings
Set these exact values in the Render setup page:
- **Name**: `psgrkcw-chatbot-backend` (or similar)
- **Region**: Choose the one closest to you (e.g., Singapore or Frankfurt).
- **Language**: `Python 3`
- **Root Directory**: `.` (leave as default)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --chdir PSGR_Chatbot/backend -b 0.0.0.0:$PORT app:app`

### 3. Verify Startup
- Watch the "Deploy Logs". 
- Once it says "Service is live", click the link provided by Render. 
- Add `/health` to the end of your Render URL (e.g., `https://your-app.onrender.com/health`).
- **Confirmation**: It should show `{"status": "ok"}`.

---

## Phase 2: Connecting and Deploying the Landing Page (Vercel)

Now we connect the website to the backend we just built.

### 1. Update the Production Link (Crucial!)
Once you have your Render URL (e.g., `https://psgrkcw-chatbot.onrender.com`), we must update your local code:
1. Open `js/config.js`.
2. Change the `API_BASE_URL` to your **Live Render URL**.
3. Save, Commit, and Push to GitHub.

### 2. Connect to Vercel
1. Log in to [vercel.com](https://vercel.com).
2. Click **Add New** > **Project**.
3. Select your GitHub repository: `PSGRKCW-talk-`.
4. **Project Settings**:
   - **Framework Preset**: `Other`
   - **Root Directory**: `.` (leave as default)
   - **Output Directory**: Leave blank (Vercel will serve your HTML files from the main folder).
5. Click **Deploy**.

---

## Phase 3: Final Testing

1. Open your live Vercel URL (e.g., `https://psgrkcw-talk.vercel.app`).
2. Open the chatbot and ask "Hi". 
   - If it replies, your connection is successful!
3. Go to `/admin-login.html` on your live site and verify the admin login works.

### Maintenance Note
- **Cold Boot**: Since we are using the Free Tier, the first time you visit the site each day, it might take 1-2 minutes for the Chatbot to wake up. This is normal for free hosting.
