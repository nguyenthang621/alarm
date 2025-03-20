import subprocess
import re
import os
from configs import config
from apscheduler.schedulers.background import BackgroundScheduler

def get_numbers_from_script(script_path):
    try:
        result = subprocess.run([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output = result.stdout
        numbers = re.findall(r'sip:(\d+)@', output)
        return set(numbers)
    except Exception as e:
        print(f"Error running script: {e}")
        return set()

def get_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            numbers = {line.strip() for line in f if line.strip()}
        return numbers
    except Exception as e:
        print(f"Error reading file: {e}")
        return set()

def compare_numbers(script_numbers, file_numbers):
    missing_numbers = file_numbers - script_numbers
    return missing_numbers

def save_missing_to_file(missing_numbers, cache_file):
    os.makedirs(os.path.dirname(cache_file), exist_ok=True)
    try:
        with open(cache_file, 'w') as f:
            for number in sorted(missing_numbers):
                f.write(f"{number}\n")
        print(f"Missing numbers saved to {cache_file}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def clear_file(cache_file):
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
    
    script_numbers = get_numbers_from_script(script_path)
    print("Numbers from script:", script_numbers)
    
    file_numbers = get_numbers_from_file(list_device)
    print("Numbers from file:", file_numbers)
    
    missing = compare_numbers(script_numbers, file_numbers)
    
    if missing:
        print("Numbers missing from script output:", missing)
        save_missing_to_file(missing, cache_file)
    else:
        print("All numbers from file are present in script output")
        if os.path.exists(cache_file):
            clear_file(cache_file)
        else:
            print(f"{cache_file} does not exist, nothing to clear")


# Init scheduler
if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(main, 'interval', seconds=int(config.SCHEDULER)) 
    scheduler.start()
    
    print("Scheduler started. Running main every 60 seconds...")
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler stopped.")