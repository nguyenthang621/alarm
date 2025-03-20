import subprocess
import re

def get_numbers_from_script(script_path):
    # Gọi shell script và lấy output
    try:
        # Sử dụng universal_newlines=True cho Python 3.5 trở xuống
        result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output = result.stdout
        
        # Tìm tất cả số bắt đầu bằng "sip:" và lấy phần số
        numbers = re.findall(r'sip:(\d+)@', output)
        return set(numbers)
    except Exception as e:
        print(f"Error running script: {e}")
        return set()

def get_numbers_from_file(file_path):
    # Đọc danh sách số từ file
    try:
        with open(file_path, 'r') as f:
            numbers = {line.strip() for line in f if line.strip()}
        return numbers
    except Exception as e:
        print(f"Error reading file: {e}")
        return set()

def compare_numbers(script_numbers, file_numbers):
    # Tìm các số có trong file nhưng không có trong output của script
    missing_numbers = file_numbers - script_numbers
    return missing_numbers

def main():
    script_path = "../test01.sh"  # Điều chỉnh đường dẫn nếu cần
    numbers_file = "data/devices.txt"   # File chứa danh sách số cần so sánh
    
    # Lấy danh sách số từ script
    script_numbers = get_numbers_from_script(script_path)
    print("Numbers from script:", script_numbers)
    
    # Lấy danh sách số từ file
    file_numbers = get_numbers_from_file(numbers_file)
    print("Numbers from file:", file_numbers)
    
    # So sánh và tìm số bị thiếu
    missing = compare_numbers(script_numbers, file_numbers)
    
    # In kết quả
    if missing:
        print("Numbers missing from script output:", missing)
    else:
        print("All numbers from file are present in script output")

if __name__ == "__main__":
    main()