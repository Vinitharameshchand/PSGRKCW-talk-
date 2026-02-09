/**
 * Admin Login Script
 * Handles authentication for FAQ management system
 */

const API_BASE = 'http://127.0.0.1:5001';

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');
    const loginBtn = document.getElementById('login-btn');
    const loginText = document.getElementById('login-text');
    const loginLoader = document.getElementById('login-loader');

    // Check if already logged in
    checkAuth();

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value;

        if (!username || !password) {
            showError('Please enter both username and password');
            return;
        }

        // Show loading state
        loginBtn.disabled = true;
        loginText.style.display = 'none';
        loginLoader.style.display = 'inline-block';
        hideError();

        try {
            const response = await fetch(`${API_BASE}/admin/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                // Store username in localStorage
                localStorage.setItem('admin_username', data.username);

                // Redirect to dashboard
                window.location.href = 'admin-dashboard.html';
            } else {
                showError(data.error || 'Invalid credentials. Please try again.');
            }
        } catch (error) {
            console.error('Login error:', error);
            showError('Connection error. Please check if the server is running.');
        } finally {
            // Reset button state
            loginBtn.disabled = false;
            loginText.style.display = 'inline';
            loginLoader.style.display = 'none';
        }
    });

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        setTimeout(() => {
            errorMessage.style.opacity = '1';
        }, 10);
    }

    function hideError() {
        errorMessage.style.opacity = '0';
        setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 300);
    }

    async function checkAuth() {
        try {
            const response = await fetch(`${API_BASE}/admin/check-auth`, {
                credentials: 'include'
            });
            const data = await response.json();

            if (data.authenticated) {
                // Already logged in, redirect to dashboard
                window.location.href = 'admin-dashboard.html';
            }
        } catch (error) {
            console.error('Auth check error:', error);
        }
    }
});
