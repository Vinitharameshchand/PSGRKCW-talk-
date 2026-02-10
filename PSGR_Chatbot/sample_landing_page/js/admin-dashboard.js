/**
 * Admin Dashboard Script
 * Manages FAQ CRUD operations
 */

const API_BASE = config.API_BASE_URL;
let currentFAQs = [];

document.addEventListener('DOMContentLoaded', () => {
    // Check authentication
    checkAuth();

    // Load initial data
    loadStats();
    loadFAQs();

    // Set up event listeners
    setupEventListeners();

    // Display username
    const username = localStorage.getItem('admin_username') || 'Admin';
    document.getElementById('admin-username').textContent = username;
});

// ============ AUTHENTICATION ============
async function checkAuth() {
    try {
        const response = await fetch(`${API_BASE}/admin/check-auth`, {
            credentials: 'include'
        });
        const data = await response.json();

        if (!data.authenticated) {
            window.location.href = 'admin-login.html';
        }
    } catch (error) {
        console.error('Auth check error:', error);
        window.location.href = 'admin-login.html';
    }
}

async function logout() {
    try {
        await fetch(`${API_BASE}/admin/logout`, {
            method: 'POST',
            credentials: 'include'
        });
        localStorage.removeItem('admin_username');
        window.location.href = 'index.html';
    } catch (error) {
        console.error('Logout error:', error);
    }
}

// ============ EVENT LISTENERS ============
function setupEventListeners() {
    // Logout button
    document.getElementById('logout-btn').addEventListener('click', logout);

    // Navigation
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const section = item.dataset.section;
            showSection(section);
        });
    });

    // Add FAQ form
    document.getElementById('add-faq-form').addEventListener('submit', addFAQ);

    // Edit FAQ form
    document.getElementById('edit-faq-form').addEventListener('submit', updateFAQ);

    // Character counter
    const replyTextarea = document.getElementById('reply');
    replyTextarea.addEventListener('input', (e) => {
        document.getElementById('char-count').textContent = e.target.value.length;
    });

    // Filter domain change
    document.getElementById('filter-domain').addEventListener('change', filterFAQs);

    // Search on enter
    document.getElementById('search-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            searchFAQs();
        }
    });
}

// ============ NAVIGATION ============
function showSection(sectionName) {
    // Hide all sections
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.remove('active');
    });

    // Remove active from all nav items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });

    // Show selected section
    const section = document.getElementById(`${sectionName}-section`);
    if (section) {
        section.classList.add('active');
    }

    // Activate nav item
    const navItem = document.querySelector(`[data-section="${sectionName}"]`);
    if (navItem) {
        navItem.classList.add('active');
    }
}

// ============ LOAD DATA ============
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE}/admin/stats`, {
            credentials: 'include'
        });
        const data = await response.json();

        if (data.success) {
            document.getElementById('total-faqs').textContent = data.stats.total_faqs;
            document.getElementById('admission-count').textContent = data.stats.by_domain.admission || 0;
            document.getElementById('hostel-count').textContent = data.stats.by_domain.hostel || 0;
            document.getElementById('fees-count').textContent = data.stats.by_domain.fees || 0;
        }
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

async function loadFAQs() {
    try {
        const listContainer = document.getElementById('faqs-list');
        listContainer.innerHTML = '<div class="loading">Loading FAQs...</div>';

        const response = await fetch(`${API_BASE}/admin/faqs`, {
            credentials: 'include'
        });
        const data = await response.json();

        if (data.success) {
            currentFAQs = data.faqs;
            displayFAQs(currentFAQs);
        } else {
            listContainer.innerHTML = '<div class="error">Failed to load FAQs</div>';
        }
    } catch (error) {
        console.error('Error loading FAQs:', error);
        document.getElementById('faqs-list').innerHTML = '<div class="error">Error loading FAQs</div>';
    }
}

function displayFAQs(faqs) {
    const listContainer = document.getElementById('faqs-list');

    if (faqs.length === 0) {
        listContainer.innerHTML = '<div class="empty-state">No FAQs found</div>';
        return;
    }

    let html = '';
    faqs.forEach((faq, index) => {
        html += `
            <div class="faq-card" data-index="${index}">
                <div class="faq-header">
                    <span class="faq-domain">${faq.domain || 'general'}</span>
                    <div class="faq-actions">
                        <button class="btn-icon" onclick="editFAQ(${index})" title="Edit">✏️</button>
                        <button class="btn-icon btn-delete" onclick="confirmDelete(${index})" title="Delete">🗑️</button>
                    </div>
                </div>
                <div class="faq-keywords">
                    ${faq.keywords.map(k => `<span class="keyword-tag">${k}</span>`).join('')}
                </div>
                <div class="faq-reply">${faq.reply}</div>
            </div>
        `;
    });

    listContainer.innerHTML = html;
}

function filterFAQs() {
    const selectedDomain = document.getElementById('filter-domain').value;

    if (!selectedDomain) {
        displayFAQs(currentFAQs);
    } else {
        const filtered = currentFAQs.filter(faq => faq.domain === selectedDomain);
        displayFAQs(filtered);
    }
}

// ============ ADD FAQ ============
async function addFAQ(e) {
    e.preventDefault();

    const form = e.target;
    const btnText = document.getElementById('add-btn-text');
    const btnLoader = document.getElementById('add-btn-loader');
    const messageDiv = document.getElementById('add-message');

    const domain = document.getElementById('domain').value;
    const keywordsInput = document.getElementById('keywords').value;
    const reply = document.getElementById('reply').value;

    // Parse keywords
    const keywords = keywordsInput.split(',').map(k => k.trim()).filter(k => k.length > 0);

    if (keywords.length === 0) {
        showMessage(messageDiv, 'Please enter at least one keyword', 'error');
        return;
    }

    // Show loading
    btnText.style.display = 'none';
    btnLoader.style.display = 'inline-block';
    form.querySelector('.btn-primary').disabled = true;

    try {
        const response = await fetch(`${API_BASE}/admin/faqs`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include',
            body: JSON.stringify({ domain, keywords, reply })
        });

        const data = await response.json();

        if (data.success) {
            showMessage(messageDiv, 'FAQ added successfully! ✅', 'success');
            form.reset();
            document.getElementById('char-count').textContent = '0';

            // Reload data
            loadStats();
            loadFAQs();

            // Reload chatbot FAQs
            await fetch(`${API_BASE}/reload-faqs`, {
                method: 'POST',
                credentials: 'include'
            });
        } else {
            showMessage(messageDiv, data.error || 'Failed to add FAQ', 'error');
        }
    } catch (error) {
        console.error('Error adding FAQ:', error);
        showMessage(messageDiv, 'Error adding FAQ. Please try again.', 'error');
    } finally {
        btnText.style.display = 'inline';
        btnLoader.style.display = 'none';
        form.querySelector('.btn-primary').disabled = false;
    }
}

// ============ EDIT FAQ ============
function editFAQ(index) {
    const faq = currentFAQs[index];

    document.getElementById('edit-index').value = index;
    document.getElementById('edit-domain').value = faq.domain;
    document.getElementById('edit-keywords').value = faq.keywords.join(', ');
    document.getElementById('edit-reply').value = faq.reply;

    document.getElementById('edit-modal').style.display = 'flex';
}

function closeEditModal() {
    document.getElementById('edit-modal').style.display = 'none';
}

async function updateFAQ(e) {
    e.preventDefault();

    const index = parseInt(document.getElementById('edit-index').value);
    const domain = document.getElementById('edit-domain').value;
    const keywordsInput = document.getElementById('edit-keywords').value;
    const reply = document.getElementById('edit-reply').value;

    const keywords = keywordsInput.split(',').map(k => k.trim()).filter(k => k.length > 0);

    try {
        const response = await fetch(`${API_BASE}/admin/faqs/${index}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include',
            body: JSON.stringify({ domain, keywords, reply })
        });

        const data = await response.json();

        if (data.success) {
            closeEditModal();
            loadFAQs();
            loadStats();

            // Reload chatbot FAQs
            await fetch(`${API_BASE}/reload-faqs`, {
                method: 'POST',
                credentials: 'include'
            });

            alert('FAQ updated successfully! ✅');
        } else {
            alert(data.error || 'Failed to update FAQ');
        }
    } catch (error) {
        console.error('Error updating FAQ:', error);
        alert('Error updating FAQ. Please try again.');
    }
}

// ============ DELETE FAQ ============
function confirmDelete(index) {
    const faq = currentFAQs[index];
    const keywords = faq.keywords.join(', ');

    if (confirm(`Are you sure you want to delete this FAQ?\n\nKeywords: ${keywords}\n\nThis action cannot be undone.`)) {
        deleteFAQ(index);
    }
}

async function deleteFAQ(index) {
    try {
        const response = await fetch(`${API_BASE}/admin/faqs/${index}`, {
            method: 'DELETE',
            credentials: 'include'
        });

        const data = await response.json();

        if (data.success) {
            loadFAQs();
            loadStats();

            // Reload chatbot FAQs
            await fetch(`${API_BASE}/reload-faqs`, {
                method: 'POST',
                credentials: 'include'
            });

            alert('FAQ deleted successfully! ✅');
        } else {
            alert(data.error || 'Failed to delete FAQ');
        }
    } catch (error) {
        console.error('Error deleting FAQ:', error);
        alert('Error deleting FAQ. Please try again.');
    }
}

// ============ SEARCH FAQ ============
async function searchFAQs() {
    const query = document.getElementById('search-input').value.trim();
    const resultsDiv = document.getElementById('search-results');

    if (!query) {
        resultsDiv.innerHTML = '<p class="empty-state">Enter a keyword to search FAQs</p>';
        return;
    }

    try {
        resultsDiv.innerHTML = '<div class="loading">Searching...</div>';

        const response = await fetch(`${API_BASE}/admin/faqs/search?q=${encodeURIComponent(query)}`, {
            credentials: 'include'
        });
        const data = await response.json();

        if (data.success) {
            if (data.results.length === 0) {
                resultsDiv.innerHTML = '<p class="empty-state">No FAQs found matching your search</p>';
            } else {
                let html = `<p class="search-count">Found ${data.results.length} result(s)</p>`;
                data.results.forEach(item => {
                    const faq = item.faq;
                    html += `
                        <div class="faq-card">
                            <div class="faq-header">
                                <span class="faq-domain">${faq.domain || 'general'}</span>
                                <div class="faq-actions">
                                    <button class="btn-icon" onclick="editFAQ(${item.index})">✏️</button>
                                </div>
                            </div>
                            <div class="faq-keywords">
                                ${faq.keywords.map(k => `<span class="keyword-tag">${k}</span>`).join('')}
                            </div>
                            <div class="faq-reply">${faq.reply}</div>
                        </div>
                    `;
                });
                resultsDiv.innerHTML = html;
            }
        }
    } catch (error) {
        console.error('Search error:', error);
        resultsDiv.innerHTML = '<div class="error">Error searching FAQs</div>';
    }
}

// ============ EXPORT ============
async function exportFAQs() {
    try {
        const response = await fetch(`${API_BASE}/admin/faqs/export`, {
            credentials: 'include'
        });
        const data = await response.json();

        if (data.success) {
            // Create downloadable file
            const blob = new Blob([JSON.stringify(data.data, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `faqs_export_${new Date().toISOString().split('T')[0]}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            alert('FAQs exported successfully! ✅');
        }
    } catch (error) {
        console.error('Export error:', error);
        alert('Error exporting FAQs');
    }
}

// ============ UTILITIES ============
function showMessage(element, message, type) {
    element.textContent = message;
    element.className = `message ${type}`;
    element.style.display = 'block';

    setTimeout(() => {
        element.style.display = 'none';
    }, 5000);
}
