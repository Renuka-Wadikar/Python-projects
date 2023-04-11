import requests
import selectorlib
import smtplib, ssl
import os, time
import sqlite3


URL = 'http://programmer100.pythonanywhere.com/tours/'

connection = sqlite3.connect('data.db')

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    message = "Subject: Upcoming Tours!\n" + message
    username = "renukawadikar27@gmail.com"
    password = os.environ['PASSWORD']

    receiver = "renukawadikar27@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def scrape(url):
    # Scrape the page source from URL
    respoonse = requests.get(url)
    source = respoonse.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("D:\Python projects\Exercises\Web Scrapping\extract.yaml")
    value = extractor.extract(source)['tours']
    return value

    
def store(extracted):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO event VALUES(?,?,?)",row)
    connection.commit()

def read(extracted):
    row = extracted.split(',')
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM event WHERE event_name=? AND city=? AND date=?',(band,city,date))
    rows = cursor.fetchall()
    print(rows)
    return rows

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        
        print(extracted)
        if extracted != 'No upcoming tours':
            data = read(extracted)
            if not data:
                store(extracted)
                send_email(extracted)
                print('email was sent!')
        time.sleep(2)
