import smtplib 
from email.message import EmailMessage

def sendEmail(recipientEmail, subject, body):
    # initialize email variables
    senderEmail = ""
    password = ""
    messg = EmailMessage()
    messg.set_content(body)
    messg['subject'] = subject  
    messg['to'] = recipientEmail
    messg['from'] = senderEmail
    # server variables
    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo() #<< will talk later
    # start TLS for security
    server.starttls()
    # Authentication
    server.login(senderEmail, password)
    # sending the mail
    # server.sendmail(senderEmail, recipientEmail, subject, body)
    server.send_message(messg)
    # terminating the session
    server.quit()

if __name__=='__main__':
    reciprecipientEmail = ""
    subject = "SPTM testing"
    body = "This message is sent to you by AYAAN from a python script"
    sendEmail(reciprecipientEmail, subject, body)