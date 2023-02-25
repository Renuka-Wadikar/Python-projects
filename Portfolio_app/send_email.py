import smtplib, ssl
from email.message import EmailMessage
import os


def sent_email(user_email,message):
    username  = 'renukawadikar27@gmail.com'
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'A new email from ' + user_email
    msg['From'] = username
    msg['To'] = username
    host = 'smtp.gmail.com'
    port = 465

    password = os.getenv('PASSWORD')
    context  = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(username, password)
        server.send_message(msg)

