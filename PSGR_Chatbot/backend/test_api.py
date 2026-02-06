import requests
import time

def test_chat():
    url = "http://127.0.0.1:5001/chat"
    questions = [
        "Hi",
        "What are the fees?",
        "Tell me about admissions",
        "Who are the top placement companies?",
        "Where is the college located?"
    ]

    print("🚀 Starting Chatbot API Test...")
    
    for q in questions:
        print(f"\nUser: {q}")
        try:
            response = requests.post(url, json={"message": q})
            if response.status_code == 200:
                print(f"Bot: {response.json().get('reply')}")
            else:
                print(f"❌ Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Connection failed: {e}")
        time.sleep(1)

if __name__ == "__main__":
    test_chat()
