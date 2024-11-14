from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Path to store the notepad text file
file_path = 'notepad.txt'

@app.route('/load-text', methods=['GET'])
def load_text():
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content, 200
    return '', 200  # Return empty if the file doesn't exist

@app.route('/save-text', methods=['POST'])
def save_text():
    data = request.json
    text = data.get('text', '')

    # Save the text to a file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return jsonify({"message": "Text saved successfully"}), 200

@app.route('/')
def serve_index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(port=5000)
