from flask import Flask, request, jsonify

app = Flask(__name__)

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

    return jsonify({
        "title": "Risk Report",
        "summary": f"This report is about {user_input}"
    })

if __name__ == "__main__":
    app.run(port=5000)