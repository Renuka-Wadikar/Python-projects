import os
import smtplib
import imghdr
from email.message import EmailMessage
PASSWORD = os.environ['PASSWORD']
SENDER = 'renukawadikar27@gmail.com'
def send_email(image):
    email_message = EmailMessage()
    email_message['Subject'] = "New Motion dectected!"
    email_message.set_content("Hey, there was a new motion detected on the camera!")
    
    with open(image,'rb') as file:
        content = file.read()
        
    email_message.add_attachment(content,maintype ='image',subtype =imghdr.what(None,content))
    
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER,SENDER,email_message.as_string())
    gmail.quit()
    print('An object enter')

if __name__ == '__main__':
    send_email(f'D:\Python projects\Portfolio_app\images\photo.jpg')