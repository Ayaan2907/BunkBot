import smtplib 
from email.message import EmailMessage

def sendEmail(recipientEmail, subject, body):
    # initialize email variables
    CONST_senderEmail = ""
    CONST_password = ""
    messg = EmailMessage()
    messg.set_content(body)
    messg['subject'] = subject  
    messg['to'] = recipientEmail
    messg['from'] = CONST_senderEmail
    # server variables
    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    server.starttls()
    print("server started...")
    # Authentication
    server.login(CONST_senderEmail, CONST_password)
    # sending the mail
    # server.sendmail(senderEmail, recipientEmail, subject, body)
    server.send_message(messg)
    print("message sent!!!")
    # terminating the session
    server.quit()
    print("server stopped...")

def main():
    reciprecipientEmail = "ayaanansari7921@outlook.com"
    subject = "SPTMlib testing"
    body = "This message is sent to you by AYAAN from a python script to test the program"
    sendEmail(reciprecipientEmail, subject, body)
    
if __name__=='__main__':
    main()