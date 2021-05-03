import notifications,  speech
import time
import json
# load json
# get the keyword and email specific data first
f = open ('config.json', 'r')
config = json.loads(f.read())
keywords = config['keywords']
reciprecipientEmail = config['reciprecipientEmail'] 
CONST_senderEmail = config['CONST_senderEmail']
CONST_EmailPassword = config['CONST_EmailPassword']
subject = config['subject']
body = config['body']
while True:
    initialCounter = time.perf_counter()
    controller = speech.audioController(keywords) 
    if(controller==1):
        notifications.sendEmail(reciprecipientEmail, CONST_senderEmail, CONST_EmailPassword, subject, body)
        finalCounter = time.perf_counter()   
        print(f" mail sent in {finalCounter - initialCounter:0.2f} seconds")
    print("======================")