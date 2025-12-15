from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from backend.chatbot_logic import find_response
import os


app = Flask(__name__)
CORS(app)

# ROOT PAGE (for browser testing)
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>College Chatbot</title></head>
    <body>
        <h1>🎓 College Chatbot Live!</h1>
        <p>Backend API is running. Check <a href="/chat">/chat</a> or your frontend.</p>
    </body>
    </html>
    """



# HEALTH CHECK (Render uses this)
@app.route('/health')
def health():
    return "OK", 200

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return "Chatbot API - Use POST with JSON {'message': 'hello'}"
    
    if request.method == 'POST':
        data = request.json
        user_message = data.get('message', '')
        response = find_response(user_message)
        return jsonify({'response': response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

