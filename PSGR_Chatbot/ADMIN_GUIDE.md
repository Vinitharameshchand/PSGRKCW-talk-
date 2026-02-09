# Admin FAQ Management System - Documentation

## 🎯 Overview
This is a comprehensive Admin FAQ Management System for PSGRKCW Chatbot that allows admission staff to add, edit, delete, and manage FAQs without touching any code.

## 📁 Project Structure

```
PSGR_Chatbot/
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── admin_routes.py           # Admin API endpoints
│   ├── data/
│   │   ├── faqs_merged.json      # Main FAQ database
│   │   └── backups/              # Automatic backups
│   └── requirements.txt
│
├── frontend/
│   ├── admin-login.html          # Admin login page
│   ├── admin-dashboard.html      # Admin dashboard
│   ├── css/
│   │   └── admin.css             # Admin styling
│   └── js/
│       ├── admin-login.js        # Login logic
│       └── admin-dashboard.js    # Dashboard logic
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Modern web browser

### Installation

1. **Backend Setup**
```bash
cd PSGR_Chatbot/backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask flask-cors scikit-learn numpy
```

2. **Start the Server**
```bash
python app.py
```
The server will run on `http://127.0.0.1:5001`

3. **Access Admin Panel**
Open your browser and go to:
```
http://127.0.0.1:3000/admin-login.html
```

## 🔐 Login Credentials

**Default Admin Accounts:**
- Username: `admin` | Password: `psgrkcw2024`
- Username: `admission` | Password: `admission2024`

⚠️ **Important:** Change these passwords in production!

To change passwords, edit `backend/admin_routes.py`:
```python
ADMIN_CREDENTIALS = {
    "your_username": "your_password"
}
```

## 📋 Features

### 1. Dashboard Overview
- View total FAQs count
- See category-wise distribution
- Quick action buttons
- Real-time statistics

### 2. Add New FAQ
- Select category (Admission, Fees, Hostel, etc.)
- Enter keywords (comma-separated)
- Write answer (max 2000 characters)
- Automatic validation
- Prevents duplicate keywords

### 3. Manage FAQs
- View all FAQs in a list
- Filter by category
- Edit any FAQ
- Delete FAQs with confirmation
- Real-time updates

### 4. Search FAQs
- Search by keyword or text
- Filter results by domain
- Quick edit from search results

### 5. Export FAQs
- Download complete FAQ database as JSON
- Includes all data fields
- Timestamped filename

## 🛡️ Security Features

1. **Session-based Authentication**
   - Secure login required
   - Auto-logout on session expiry
   - Protected API routes

2. **Input Validation**
   - Prevents empty submissions
   - Character limits enforced
   - Duplicate detection
  - SQL injection protection (JSON-based)

3. **Automatic Backups**
   - Creates backup before each save
   - Keeps last 10 backups
   - Located in `data/backups/`

## 📖 User Guide (For Admission Staff)

### How to Add a New FAQ

1. **Login** to admin panel
2. Click **"Add New FAQ"** in sidebar
3. Fill in the form:
   - **Category**: Choose appropriate category
   - **Keywords**: Enter search terms students might use (e.g., "admission, apply, how to join")
   - **Answer**: Write the complete answer
4. Click **"Add FAQ"**
5. Success message will appear
6. FAQ is immediately available in chatbot

### How to Edit an FAQ

1. Go to **"Manage FAQs"**
2. Find the FAQ you want to edit
3. Click the **✏️ (edit)** icon
4. Update the information in the modal
5. Click **"Save Changes"**
6. Changes are immediately reflected

### How to Delete an FAQ

1. Go to **"Manage FAQs"**
2. Find the FAQ you want to delete
3. Click the **🗑️ (delete)** icon
4. Confirm deletion in the popup
5. FAQ is permanently removed

### How to Search FAQs

1. Go to **"Search FAQs"**
2. Enter keyword in search box
3. Press Enter or click **"Search"**
4. Results will display matching FAQs
5. You can edit directly from search results

## 🔧 API Endpoints

### Authentication
- `POST /admin/login` - Admin login
- `POST /admin/logout` - Admin logout
- `GET /admin/check-auth` - Check authentication status

### FAQ Management
- `GET /admin/faqs` - Get all FAQs
- `POST /admin/faqs` - Add new FAQ
- `PUT /admin/faqs/<index>` - Update FAQ
- `DELETE /admin/faqs/<index>` - Delete FAQ
- `GET /admin/faqs/search?q=<query>` - Search FAQs

### Utilities
- `GET /admin/stats` - Get FAQ statistics
- `GET /admin/faqs/export` - Export FAQs as JSON
- `POST /reload-faqs` - Reload FAQs in chatbot

## 📊 JSON Structure

Each FAQ follows this structure:

```json
{
  "domain": "admission",
  "keywords": ["admission", "apply", "how to join"],
  "reply": "Admission is done mainly through online application..."
}
```

**Fields:**
- `domain`: Category of the FAQ (required)
- `keywords`: Array of search terms (required, at least 1)
- `reply`: The answer text (required, max 2000 chars)

## 🎨 Customization

### Changing Colors
Edit `frontend/css/admin.css`:

```css
:root {
    --primary-color: #8547B0;  /* Main purple */
    --secondary-color: #2C2081; /* Deep blue */
    --accent-pink: #F89BDD;     /* Pink accent */
}
```

### Adding New Categories
Edit both files:

1. **frontend/admin-dashboard.html** - Add option to dropdowns
2. **backend/admin_routes.py** - No changes needed (dynamic)

## 🐛 Troubleshooting

### Issue: Cannot login
**Solution:**
- Check if backend server is running
- Verify credentials are correct
- Check browser console for errors
- Clear browser cache/cookies

### Issue: FAQs not updating in chatbot
**Solution:**
- FAQs auto-reload after each change
- If not working, restart backend server
- Check `faqs_merged.json` file permissions

### Issue: "Connection error" message
**Solution:**
- Ensure backend is running on port 5001
- Check firewall settings
- Verify CORS is enabled

### Issue: Backup files filling up
**Solution:**
- System keeps only 10 most recent backups
- Manually delete old backups from `data/backups/`

## 📱 Mobile Support

The admin panel is fully responsive and works on:
- Desktop browsers
- Tablets
- Mobile phones (landscape recommended)

## ⚙️ Configuration

### Change Server Port
Edit `backend/app.py`:
```python
app.run(port=5001, debug=True)
```

### Change Session Timeout
Edit `backend/app.py`:
```python
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
```

### Enable/Disable Auto-Backup
Edit `backend/admin_routes.py`:
```python
def save_faqs(faqs):
    # Comment out backup lines to disable
    # backup_filename = ...
    # shutil.copy2(FAQ_FILE, backup_filename)
```

## 📞 Support

For technical issues or questions:
- Contact IT Support
- Email: it@psgrkcw.ac.in
- Phone: 080-49251252

## 📝 Best Practices

1. **Keywords:**
   - Use simple, common words
   - Include variations (e.g., "fee", "fees", "cost")
   - Add question words (what, how, when)

2. **Answers:**
   - Be clear and concise
   - Include links where relevant
   - Use proper formatting
   - Update regularly

3. **Categories:**
   - Choose the most relevant category
   - Be consistent with categorization
   - Use "general" for misc topics

4. **Security:**
   - Change default passwords immediately
   - Logout after use
   - Don't share credentials
   - Use strong passwords

## 🔄 Backup & Recovery

### Manual Backup
1. Go to Dashboard → Export FAQs
2. Save the downloaded JSON file
3. Store in a safe location

### Restore from Backup
1. Open `backend/data/faqs_merged.json`
2. Replace content with backup JSON
3. Restart backend server

### Automatic Backups
- Created before every save operation
- Located in `data/backups/`
- Named with timestamp: `faqs_backup_YYYYMMDD_HHMMSS.json`
- Last 10 backups kept automatically

## 🚀 Production Deployment

### Security Checklist
- [ ] Change all default passwords
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS
- [ ] Set secure session keys
- [ ] Restrict IP access if possible
- [ ] Regular backups to external storage
- [ ] Monitor login attempts

### Performance Tips
- Use production WSGI server (gunicorn, uwsgi)
- Enable gzip compression
- Set appropriate cache headers
- Monitor backup directory size

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Developed for:** PSGR Krishnammal College for Women
