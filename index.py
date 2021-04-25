import notifications
import speech, time 
# import time as t

# initialized SENDER variables WHICH SHOULD BE CHANGED ACCORDINGLY
CONST_senderEmail = "initialize_me"
CONST_password = "initialize_me"
reciprecipientEmail = "initialize_me"

subject = "Finalising changes"
body = """
        This message is sent to you by AYAAN from a python script to test the final steps program
    """
# hard coding the keywords
keyWord0 = "send"    
keyWord1 = "interesting"       
while True:
    controller = speech.audioController(keyWord0, keyWord1)
    if(controller == 1):
        tic = time.perf_counter()
        notifications.sendEmail(reciprecipientEmail, CONST_senderEmail, CONST_password, subject, body)
        # notifications.main()
        toc = time.perf_counter()
        print(f" mail sent in {toc - tic:0.2f} seconds")
    elif(controller==0):
        print("process terminated!")
        break
    print("======================")