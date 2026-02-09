import requests
import time

def test_chat():
    url = "http://127.0.0.1:5001/chat"
    questions = [
        "What is the admission process?",
        "What are the college timings?",
        "Is there a dress code?",
        "Who is the principal of PSGRKCW?",
        "How are the lab facilities?"
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
