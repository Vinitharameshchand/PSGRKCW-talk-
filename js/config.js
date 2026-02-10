// Smart configuration: Auto-detects local vs production environment
const config = {
    API_BASE_URL: (() => {
        // If running on localhost or 127.0.0.1, use local backend
        if (window.location.hostname === 'localhost' ||
            window.location.hostname === '127.0.0.1') {
            return 'http://127.0.0.1:5001';
        }
        // Otherwise, use production Render backend
        return 'https://psgrkcw-chatbot-backend.onrender.com';
    })()
};
