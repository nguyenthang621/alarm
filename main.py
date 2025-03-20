import subprocess
import re
import os
from configs import config

def get_numbers_from_script(script_path):
    # Excute script and return numbers
    try:
        # use to python ver < 3.5
        result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output = result.stdout
        numbers = re.findall(r'sip:(\d+)@', output)
        return set(numbers)
    except Exception as e:
        print(f"Error running script: {e}")
        return set()

def get_numbers_from_file(file_path):
    # read device id from file
    try:
        with open(file_path, 'r') as f:
            numbers = {line.strip() for line in f if line.strip()}
        return numbers
    except Exception as e:
        print(f"Error reading file: {e}")
        return set()

def compare_numbers(script_numbers, file_numbers):
    # compare numbers
    missing_numbers = file_numbers - script_numbers
    return missing_numbers

def save_missing_to_file(missing_numbers, cache_file):
    # Tạo thư mục data nếu chưa tồn tại
    os.makedirs(os.path.dirname(cache_file), exist_ok=True)
    
    # Ghi các số bị miss vào file
    try:
        with open(cache_file, 'w') as f:
            for number in sorted(missing_numbers):
                f.write(f"{number}\n")
        print(f"Missing numbers saved to {cache_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def clear_file(cache_file):
    # Clear cache 
    try:
        with open(cache_file, 'w') as f:
            f.write("")  
        print(f"Cleared {cache_file}")
    except Exception as e:
        print(f"Error clearing file: {e}")

def main():
    script_path = config.SCRIPT_FILE  
    list_device = config.LIST_DEVICE   
    cache_file = config.CACHE_FILE
    
    # get numbers from script
    script_numbers = get_numbers_from_script(script_path)
    print("Numbers from script:", script_numbers)
    
    # get numbers from file
    file_numbers = get_numbers_from_file(list_device)
    print("Numbers from file:", file_numbers)
    
    # compare numbers missing
    missing = compare_numbers(script_numbers, file_numbers)
    
    if missing:
        print("Numbers missing from script output:", missing)
        save_missing_to_file(missing, cache_file)
    else:
        print("All numbers from file are present in script output")
        # if all numbers are present, clear the cache file
        if os.path.exists(cache_file):
            clear_file(cache_file)
        else:
            print(f"{cache_file} does not exist, nothing to clear")

if __name__ == "__main__":
    main()