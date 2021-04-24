import smtplib 
# import email.message as EmailMessage

def sendEmail(recipientEmail, message):
    # initialize sender
    senderEmail = "enter_your_email"
    password = "enter_your_password"
    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #<< will talk later
    # start TLS for security
    server.starttls()
    # Authentication
    server.login(senderEmail, password)
    # sending the mail
    server.sendmail(senderEmail, recipientEmail, message)
    # terminating the session
    server.quit()

if __name__=='__main__':
    reciprecipientEmail = "enter_recipient's_email"
    message =" someone is calling u in class"
    sendEmail(reciprecipientEmail, message)