"""
Admin FAQ Management Routes
Handles authentication and CRUD operations for FAQ management
"""

from flask import jsonify, request, session
from functools import wraps
import json
import os
from datetime import datetime
import shutil

# Admin credentials (In production, use environment variables or database)
ADMIN_CREDENTIALS = {
    "admin": "psgrkcw2024",  # Change this password in production
    "admission": "admission2024"
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE = os.path.join(BASE_DIR, "data/faqs_merged.json")
BACKUP_DIR = os.path.join(BASE_DIR, "data/backups")

# Ensure backup directory exists
os.makedirs(BACKUP_DIR, exist_ok=True)

# ---------------- DECORATORS ----------------
def login_required(f):
    """Decorator to protect admin routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check session first (for localhost)
        if session.get('admin_logged_in'):
            return f(*args, **kwargs)
        
        # Check Authorization header (for cross-domain)
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.replace('Bearer ', '')
            # Validate token
            import hashlib
            import time
            for username, password in ADMIN_CREDENTIALS.items():
                token_string = f"{username}:{password}:{int(time.time() // 3600)}"
                valid_token = hashlib.sha256(token_string.encode()).hexdigest()
                if token == valid_token:
                    return f(*args, **kwargs)
        
        return jsonify({"error": "Unauthorized. Please login."}), 401
    return decorated_function

# ---------------- HELPER FUNCTIONS ----------------
def load_faqs():
    """Load FAQs from JSON file"""
    try:
        if os.path.exists(FAQ_FILE):
            with open(FAQ_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        print(f"Error loading FAQs: {e}")
        return []

def save_faqs(faqs):
    """Save FAQs to JSON file with backup"""
    try:
        # Create backup before saving
        backup_filename = f"{BACKUP_DIR}/faqs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        if os.path.exists(FAQ_FILE):
            shutil.copy2(FAQ_FILE, backup_filename)
        
        # Save new data
        with open(FAQ_FILE, 'w', encoding='utf-8') as f:
            json.dump(faqs, f, indent=4, ensure_ascii=False)
        
        # Keep only last 10 backups
        cleanup_old_backups()
        return True
    except Exception as e:
        print(f"Error saving FAQs: {e}")
        return False

def cleanup_old_backups():
    """Keep only the 10 most recent backups"""
    try:
        backups = sorted(
            [f for f in os.listdir(BACKUP_DIR) if f.startswith('faqs_backup_')],
            reverse=True
        )
        for old_backup in backups[10:]:
            os.remove(os.path.join(BACKUP_DIR, old_backup))
    except Exception as e:
        print(f"Error cleaning backups: {e}")

def validate_faq(faq_data):
    """Validate FAQ data"""
    errors = []
    
    if not faq_data.get('domain'):
        errors.append("Domain is required")
    
    if not faq_data.get('keywords') or len(faq_data.get('keywords', [])) == 0:
        errors.append("At least one keyword is required")
    
    if not faq_data.get('reply'):
        errors.append("Reply/Answer is required")
    elif len(faq_data['reply']) > 2000:
        errors.append("Answer is too long (max 2000 characters)")
    
    # Validate keywords
    keywords = faq_data.get('keywords', [])
    if any(len(k.strip()) == 0 for k in keywords):
        errors.append("Keywords cannot be empty")
    
    return errors

# ---------------- ROUTES ----------------
def init_admin_routes(app):
    """Initialize admin routes"""
    
    @app.route('/admin/login', methods=['POST'])
    def admin_login():
        """Admin login endpoint"""
        try:
            data = request.get_json()
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()
            
            if username in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[username] == password:
                # Set session for same-domain (localhost)
                session['admin_logged_in'] = True
                session['admin_username'] = username
                
                # Generate simple token for cross-domain (Vercel to Render)
                import hashlib
                import time
                token_string = f"{username}:{password}:{int(time.time() // 3600)}"
                auth_token = hashlib.sha256(token_string.encode()).hexdigest()
                
                return jsonify({
                    "success": True,
                    "message": "Login successful",
                    "username": username,
                    "auth_token": auth_token  # Token for cross-domain auth
                })
            else:
                return jsonify({
                    "success": False,
                    "error": "Invalid username or password"
                }), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/admin/logout', methods=['POST'])
    def admin_logout():
        """Admin logout endpoint"""
        session.clear()
        return jsonify({"success": True, "message": "Logged out successfully"})
    
    @app.route('/admin/check-auth', methods=['GET'])
    def check_auth():
        """Check if admin is authenticated"""
        # Check session first (for localhost)
        if session.get('admin_logged_in'):
            return jsonify({
                "authenticated": True,
                "username": session.get('admin_username', '')
            })
        
        # Check Authorization header (for cross-domain)
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.replace('Bearer ', '')
            # Validate token
            import hashlib
            import time
            for username, password in ADMIN_CREDENTIALS.items():
                token_string = f"{username}:{password}:{int(time.time() // 3600)}"
                valid_token = hashlib.sha256(token_string.encode()).hexdigest()
                if token == valid_token:
                    return jsonify({
                        "authenticated": True,
                        "username": username
                    })
        
        return jsonify({
            "authenticated": False,
            "username": ''
        })
    
    @app.route('/admin/faqs', methods=['GET'])
    @login_required
    def get_all_faqs():
        """Get all FAQs for admin dashboard"""
        try:
            faqs = load_faqs()
            return jsonify({
                "success": True,
                "faqs": faqs,
                "total": len(faqs)
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/admin/faqs', methods=['POST'])
    @login_required
    def add_faq():
        """Add a new FAQ"""
        try:
            data = request.get_json()
            
            # Validate input
            errors = validate_faq(data)
            if errors:
                return jsonify({"success": False, "errors": errors}), 400
            
            # Create FAQ object
            new_faq = {
                "domain": data['domain'].strip(),
                "keywords": [k.strip().lower() for k in data['keywords']],
                "reply": data['reply'].strip()
            }
            
            # Load existing FAQs
            faqs = load_faqs()
            
            # Check for duplicate keywords
            existing_keywords = set()
            for faq in faqs:
                existing_keywords.update([k.lower() for k in faq.get('keywords', [])])
            
            for keyword in new_faq['keywords']:
                if keyword in existing_keywords:
                    return jsonify({
                        "success": False,
                        "error": f"Keyword '{keyword}' already exists in another FAQ"
                    }), 400
            
            # Add new FAQ
            faqs.append(new_faq)
            
            # Save to file
            if save_faqs(faqs):
                return jsonify({
                    "success": True,
                    "message": "FAQ added successfully",
                    "faq": new_faq
                })
            else:
                return jsonify({"error": "Failed to save FAQ"}), 500
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/admin/faqs/<int:index>', methods=['PUT'])
    @login_required
    def update_faq(index):
        """Update an existing FAQ"""
        try:
            data = request.get_json()
            
            # Validate input
            errors = validate_faq(data)
            if errors:
                return jsonify({"success": False, "errors": errors}), 400
            
            # Load existing FAQs
            faqs = load_faqs()
            
            if index < 0 or index >= len(faqs):
                return jsonify({"error": "FAQ not found"}), 404
            
            # Update FAQ
            faqs[index] = {
                "domain": data['domain'].strip(),
                "keywords": [k.strip().lower() for k in data['keywords']],
                "reply": data['reply'].strip()
            }
            
            # Save to file
            if save_faqs(faqs):
                return jsonify({
                    "success": True,
                    "message": "FAQ updated successfully",
                    "faq": faqs[index]
                })
            else:
                return jsonify({"error": "Failed to save FAQ"}), 500
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/admin/faqs/<int:index>', methods=['DELETE'])
    @login_required
    def delete_faq(index):
        """Delete an FAQ"""
        try:
            # Load existing FAQs
            faqs = load_faqs()
            
            if index < 0 or index >= len(faqs):
                return jsonify({"error": "FAQ not found"}), 404
            
            # Remove FAQ
            deleted_faq = faqs.pop(index)
            
            # Save to file
            if save_faqs(faqs):
                return jsonify({
                    "success": True,
                    "message": "FAQ deleted successfully",
                    "deleted": deleted_faq
                })
            else:
                return jsonify({"error": "Failed to save changes"}), 500
                
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/admin/faqs/search', methods=['GET'])
    @login_required
    def search_faqs():
        """Search FAQs by keyword or domain"""
        try:
            query = request.args.get('q', '').lower().strip()
            domain = request.args.get('domain', '').strip()
            
            faqs = load_faqs()
            results = []
            
            for idx, faq in enumerate(faqs):
                # Check domain filter
                if domain and faq.get('domain', '') != domain:
                    continue
                
                # Check search query
                if query:
                    keywords_match = any(query in k.lower() for k in faq.get('keywords', []))
                    reply_match = query in faq.get('reply', '').lower()
                    
                    if keywords_match or reply_match:
                        results.append({"index": idx, "faq": faq})
                else:
                    results.append({"index": idx, "faq": faq})
            
            return jsonify({
                "success": True,
                "results": results,
                "total": len(results)
            })
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/admin/faqs/export', methods=['GET'])
    @login_required
    def export_faqs():
        """Export FAQs as JSON file"""
        try:
            faqs = load_faqs()
            return jsonify({
                "success": True,
                "data": faqs,
                "exported_at": datetime.now().isoformat()
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/admin/stats', methods=['GET'])
    @login_required
    def get_stats():
        """Get FAQ statistics"""
        try:
            faqs = load_faqs()
            
            # Count by domain
            domain_counts = {}
            for faq in faqs:
                domain = faq.get('domain', 'unknown')
                domain_counts[domain] = domain_counts.get(domain, 0) + 1
            
            return jsonify({
                "success": True,
                "stats": {
                    "total_faqs": len(faqs),
                    "by_domain": domain_counts,
                    "last_updated": datetime.fromtimestamp(
                        os.path.getmtime(FAQ_FILE)
                    ).isoformat() if os.path.exists(FAQ_FILE) else None
                }
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
