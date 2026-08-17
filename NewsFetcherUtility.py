# 1 Exercise 10
# 2 Use the NewsAPI and the requests module to fetch the daily news related to different topics.
# 3 Go to: https://newsapi.org/
# 4 and explore the various options to build you application

import requests

api_key = "0aee511e1bf54dfb98fa46b794228394"
query = input("what type of news are you intersted in?")
url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
response = requests.get(url)
print(response.status_code)
news_data = response.json()
print(news_data.keys())

for article in news_data['articles']:
    print(article['title'])
    print(article['description'])
    print(article['url'])
    print("-" * 45 + "\n")