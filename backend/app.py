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
    
    # POST request from frontend
    data = request.get_json()  # ← Use get_json() not request.json
    if not data:
        return jsonify({'error': 'No JSON data'}), 400
    
    message = data.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        response = find_response(message)
    except Exception as e:
        return jsonify({'error': f'Chat error: {str(e)}'})
    
    return jsonify({'response': response})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

