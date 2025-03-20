from flask import Flask, render_template, jsonify
import os
from configs import config  # Giả sử config chứa CACHE_FILE và LIST_DEVICE

app = Flask(__name__)

def get_numbers_from_file(file_path):
    """Đọc danh sách số từ file và trả về set"""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return {line.strip() for line in f if line.strip()}
        return set()
    except Exception as e:
        return {f"Error reading file: {e}"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/missing-numbers')
def get_missing_numbers():
    cache_file = config.CACHE_FILE  # data/current_state_down.txt
    list_device_file = config.LIST_DEVICE  # data/devices.txt
    
    # Lấy danh sách số từ cả hai file
    missing_numbers = get_numbers_from_file(cache_file)
    all_devices = get_numbers_from_file(list_device_file)
    
    # Tổng số thiết bị
    total_cache = len(missing_numbers) if not any(n.startswith("Error") for n in missing_numbers) else 0
    total_devices = len(all_devices) if not any(n.startswith("Error") for n in all_devices) else 0
    
    return jsonify({
        "numbers": list(missing_numbers),  # Chuyển set thành list để jsonify
        "total_cache": total_cache,        # Tổng số thiết bị down
        "total_devices": total_devices     # Tổng số thiết bị trong danh sách
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)