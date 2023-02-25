import requests
from send_email import send_email

url = 'https://newsapi.org/v2/top-headlines?'\
        'sources=bbc-news&'\
        'apiKey=674d44c0db1641dcb8c95e74e573bf34'
api_key = '674d44c0db1641dcb8c95e74e573bf34'

# Make request
request = requests.get(url)

#create dictionary
content = request.json()
#creating the body of email

email_msg = ''
for article in content['articles']:
    if article['title'] is not None:
        email_msg = email_msg + article['title'] + '\n' + article['description'] + '\n'+ article['url'] + '\n\n'
    
send_email(email_msg)

