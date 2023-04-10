import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    message = "Subject: Today's news \n" + message
    username = "renukawadikar27@gmail.com"
    password = os.environ['PASSWORD']

    receiver = "renukawadikar27@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)