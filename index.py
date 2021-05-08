from speech import *
from teamAutomation import *
import time
import json

def load_config():
    global config
    with open('config.json', encoding='utf-8') as json_data_file:
        config = json.load(json_data_file)
load_config()

keywords = config['keywords']
reciprecipientEmail = config['reciprecipientEmail'] 
CONST_senderEmail = config['CONST_senderEmail']
CONST_EmailPassword = config['CONST_EmailPassword']
subject = config['subject']
body = config['body']

while True:
    print("entered while")
    initialCounter = time.perf_counter()
    controller = audioController(keywords) 
    if(controller==1):
        sendEmail(reciprecipientEmail, CONST_senderEmail, CONST_EmailPassword, subject, body)
        finalCounter = time.perf_counter()   
        print(f" mail sent in {finalCounter - initialCounter:0.2f} seconds")
    print("======================")