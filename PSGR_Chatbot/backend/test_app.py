from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "HOME WORKING"})

@app.route("/chat", methods=["POST"])
def chat():
    return jsonify({"reply": "CHAT WORKING"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
