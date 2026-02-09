# 🎓 PSGR Chatbot - Admin FAQ Management System

A complete, production-ready admin panel for managing chatbot FAQs without touching code.

## 🚀 Quick Access

**Admin Panel:** http://127.0.0.1:3000/admin-login.html

**Default Login:**
- Username: `admin` | Password: `psgrkcw2024`
- Username: `admission` | Password: `admission2024`

## ✨ What It Does

- ➕ Add new FAQs with categories and keywords
- ✏️ Edit existing FAQs
- 🗑️ Delete FAQs with confirmation
- 🔍 Search FAQs by keyword
- 💾 Export FAQ database as JSON
- 📊 View statistics by category
- 🔐 Secure login system
- 💾 Automatic backups

## 📁 Project Structure

```
PSGR_Chatbot/
├── backend/
│   ├── app.py                # Main Flask app (updated)
│   ├── admin_routes.py       # Admin API endpoints (NEW)
│   └── data/
│       ├── faqs_merged.json  # FAQ database
│       └── backups/          # Auto-backups (NEW)
│
├── frontend/
│   ├── admin-login.html      # Login page (NEW)
│   ├── admin-dashboard.html  # Dashboard (NEW)
│   ├── css/
│   │   └── admin.css         # Admin styling (NEW)
│   └── js/
│       ├── admin-login.js    # Login logic (NEW)
│       └── admin-dashboard.js # Dashboard logic (NEW)
│
├── ADMIN_GUIDE.md            # Full documentation (NEW)
└── QUICKSTART.md             # Quick start guide (NEW)
```

## 🎯 Features

### For Non-Technical Users
- ✅ Simple web interface
- ✅ No coding required
- ✅ Clear error messages
- ✅ Instant validation
- ✅ Mobile-friendly

### For Security
- ✅ Password-protected
- ✅ Session management
- ✅ Input validation
- ✅ Automatic backups
- ✅ Duplicate prevention

### For Reliability
- ✅ Real-time updates
- ✅ Backup before save
- ✅ Error handling
- ✅ Data validation
- ✅ Auto-reload chatbot

## 📖 Usage Example

### Adding a FAQ:
1. Login to admin panel
2. Click "Add New FAQ"
3. Fill form:
   - **Category:** Admission
   - **Keywords:** `admission fees, fee structure, semester cost`
   - **Answer:** `Fees vary by course. Visit college office for specific details.`
4. Click "Add FAQ"
5. ✅ Instantly available in chatbot!

## 🔧 API Endpoints

```
POST   /admin/login          - Admin login
POST   /admin/logout         - Logout
GET    /admin/check-auth     - Check auth status
GET    /admin/faqs           - Get all FAQs
POST   /admin/faqs           - Add new FAQ
PUT    /admin/faqs/<index>   - Update FAQ
DELETE /admin/faqs/<index>   - Delete FAQ
GET    /admin/faqs/search    - Search FAQs
GET    /admin/stats          - Get statistics
GET    /admin/faqs/export    - Export as JSON
POST   /reload-faqs          - Reload FAQ database
```

## 🛡️ Security

⚠️ **Change default passwords immediately!**

Edit `backend/admin_routes.py`:
```python
ADMIN_CREDENTIALS = {
    "your_username": "your_secure_password"
}
```

## 📱 Screenshots

### Login Page
- Clean, professional design
- PSGRKCW branding
- Error handling

### Dashboard
- Overview with statistics
- Category-wise FAQ count
- Quick action buttons

### Add FAQ
- Simple form interface
- Category dropdown
- Keyword input
- Character counter

### Manage FAQs
- List view with filters
- Edit/Delete buttons
- Domain tags
- Keyword tags

### Search
- Real-time search
- Filter by category
- Edit from results

## 🎨 Design

- Modern, clean UI
- PSGRKCW college colors (purple gradient)
- Responsive layout
- Smooth animations
- Mobile-optimized

## 📊 JSON Structure

```json
{
  "domain": "admission",
  "keywords": ["admission", "apply online", "how to join"],
  "reply": "Admission is done through online application..."
}
```

## 🚦 Status

✅ **Backend:** Running on port 5001  
✅ **Frontend:** Running on port 3000  
✅ **Admin Panel:** Fully functional  
✅ **Auto-Backup:** Enabled  
✅ **Documentation:** Complete  

## 📞 Support

- **Documentation:** See `ADMIN_GUIDE.md`
- **Quick Start:** See `QUICKSTART.md`
- **Email:** admission@psgrkcw.ac.in
- **Phone:** 080 49251252

## 🎓 For Admission Staff

This system is designed for **you**! No technical knowledge needed.

**You can:**
- Add FAQs when students ask new questions
- Update FAQs when information changes
- Remove outdated FAQs
- Search and organize FAQs
- Export data for backup

**You cannot:**
- Break the chatbot (safe design)
- Lose data (automatic backups)
- Create duplicates (validation)

## 🔄 Workflow

1. Student asks question not in FAQ
2. Staff adds it via admin panel
3. FAQ is instantly available
4. Backup is automatically created
5. Chatbot serves the answer

## 🏆 Benefits

- ⚡ **Fast:** Add FAQs in seconds
- 🔒 **Secure:** Password-protected
- 💾 **Safe:** Auto-backups
- 📱 **Accessible:** Works on any device
- 🎯 **Simple:** No training needed
- ✅ **Reliable:** Production-ready

---

**Built with ❤️ for PSGR Krishnammal College for Women**

*Empowering admission staff to manage chatbot knowledge independently*
