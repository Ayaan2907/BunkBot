import notifications,  speech
# , playAudio
import time

# initialized SENDER variables WHICH SHOULD BE CHANGED ACCORDINGLY
CONST_senderEmail = "munawarsayed0908@gmail.com"
CONST_password = ""
reciprecipientEmail = "munawarsayed0908@gmail.com"
subject = "Testing OCassistant"
body = f"""
        This message is sent by AYAAN from a python script to test the script.

        Someone is calling you in the class.
        """
keywords = ["ayaan", "68", "iron"] 

while True:
    initialCounter = time.perf_counter()
    controller = speech.audioController(keywords) 
    if(controller==1):
        notifications.sendEmail(reciprecipientEmail, CONST_senderEmail, CONST_password, subject, body)
        finalCounter = time.perf_counter()   
        print(f" mail sent in {finalCounter - initialCounter:0.2f} seconds")
    print("======================")