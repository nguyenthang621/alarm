from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Route chính để render giao diện
@app.route('/')
def index():
    return render_template('index.html')

# API route để lấy dữ liệu từ file
@app.route('/api/missing-numbers')
def get_missing_numbers():
    file_path = "data/cache.txt"
    missing_numbers = []
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                missing_numbers = [line.strip() for line in f if line.strip()]
        else:
            missing_numbers = ["File not found"]
    except Exception as e:
        missing_numbers = [f"Error reading file: {e}"]
    
    return jsonify({"numbers": missing_numbers})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)