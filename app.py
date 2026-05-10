from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "AI Service Running Successfully 🚀"

# NEW API
@app.route('/describe', methods=['POST'])
def describe():
    data = request.json
    user_input = data.get("input")

    # simple logic (AI will come later)
    response = f"This is a risk related to: {user_input}"

    return jsonify({
        "description": response,
        "status": "success"
    })
@app.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.json
    user_input = data.get("input")

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "user", "content": user_input}
                ]
            }
        )

        result = response.json()
        ai_output = result["choices"][0]["message"]["content"]
    
        

    except:
        ai_output = "AI not working"
@app.route('/chat', methods=['POST'])
def chat():

        data = request.json

        user_message = data.get("message")

        ai_response = f"AI response to:{user_message}"
        return jsonify({
            "response": f"You said: {user_message}"
        })

        return jsonify({
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(port=5000)