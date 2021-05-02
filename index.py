import notifications,  speech
import time
from parameters import *

while True:
    initialCounter = time.perf_counter()
    controller = speech.audioController(keywords) 
    if(controller==1):
        notifications.sendEmail(reciprecipientEmail, CONST_senderEmail, CONST_EmailPassword, subject, body)
        finalCounter = time.perf_counter()   
        print(f" mail sent in {finalCounter - initialCounter:0.2f} seconds")
    print("======================")