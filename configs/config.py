import os 
from dotenv import load_dotenv

load_dotenv()

SCRIPT_FILE = os.getenv('SCRIPT_FILE')
LIST_DEVICE = os.getenv('LIST_DEVICE')
CACHE_FILE = os.getenv('CACHE_FILE') 
SCHEDULER = os.getenv('SCHEDULER') 



if __name__ == '__main__':
    print(CACHE_FILE)