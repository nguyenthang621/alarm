import os 
from dotenv import load_dotenv

load_dotenv()

API_CHECK = os.getenv('API_CHECK')
ID_TELEGRAM = os.getenv('ID_TELEGRAM')
TOKEN_API_TELEGRAM = os.getenv('TOKEN_API_TELEGRAM') 
THRESHOLD_SEND_WARNING = os.getenv('THRESHOLD_SEND_WARNING') 
THRESHOLD_BLOCK_MAIL = os.getenv('THRESHOLD_BLOCK_MAIL') 
HOST_SERVER_MAIL = os.getenv('HOST_SERVER_MAIL') 

SPLUNK_HOST = os.getenv('SPLUNK_HOST') 
SPLUNK_PORT = os.getenv('SPLUNK_PORT') 
EARLIEST_TIME = os.getenv('EARLIEST_TIME') 
SPLUNK_USERNAME = os.getenv('SPLUNK_USERNAME') 
SPLUNK_PASSWORD = os.getenv('SPLUNK_PASSWORD') 
FILTER_NAME = os.getenv('FILTER_NAME') 
MAX_SIZE_LOGS_FILE = os.getenv('MAX_SIZE_LOGS_FILE') 



if __name__ == '__main__':
    print(API_CHECK)