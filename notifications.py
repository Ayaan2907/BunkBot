import smtplib 
from email.message import EmailMessage

def sendEmail(recipientEmail,  CONST_senderEmail, CONST_password, subject, body):
    # composing the message
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
    print("Server started...")
    # Authentication
    server.login(CONST_senderEmail, CONST_password)
    # sending the mail
    # server.sendmail(senderEmail, recipientEmail, subject, body)
    server.send_message(messg)
    print(f"Message sent to {CONST_senderEmail}!!!")
    # terminating the session
    server.quit()
    print("Server stopped...")

# if __name__=='__main__':