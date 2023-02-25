import requests

url = 'https://newsapi.org/v2/top-headlines?'\
        'sources=bbc-news&'\
        'apiKey=674d44c0db1641dcb8c95e74e573bf34'
api_key = '674d44c0db1641dcb8c95e74e573bf34'

# Make request
request = requests.get(url)

#create dictionary
content = request.json()
for article in content['articles']:
    print(article['title'])