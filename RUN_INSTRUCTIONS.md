# 🚀 How to Run the PSGRKCW Chatbot Application

Follow these steps to get the backend server and the modern chatbot interface running on your local machine.

## **Step 1: Open Terminal and Navigate to Backend**
Open your terminal and go to the project's backend directory:
```bash
cd /Users/vinitha/PSGRKCW-talk-/PSGR_Chatbot/backend
```

## **Step 2: Activate the Virtual Environment**
Activate the pre-configured environment where all the smart NLP libraries are installed:
```bash
source venv/bin/activate
```

## **Step 3: Start the Flask Server**
Run the backend API. This server handles the "brain" of the chatbot using TF-IDF statistical matching:
```bash
python3 app.py
```
*You should see a message saying: `* Running on http://127.0.0.1:5001`*

## **Step 4: Launch the Chatbot UI**
While keeping the terminal running, open the following file in your web browser (Chrome, Safari, or Edge):
```text
/Users/vinitha/PSGRKCW-talk-/PSGR_Chatbot/frontend/modern_chat.html
```
*Simply drag and drop this file into your browser.*

---

## **💡 Testing the Bot**
Once both are running, you can try typing these questions:
1. "Hello"
2. "What are the admission criteria?"
3. "Tell me about the fee structure"
4. "Where is the college located?"
5. "What are the placement opportunities?"

## **🛠 Troubleshooting**
- **"Connection Failed" in Browser**: Ensure the terminal is still running and showing `Running on http://127.0.0.1:5001`.
- **Port 5001 busy**: If you get an error that the port is in use, stop any other running python instances with `CTRL+C` in the terminal.
