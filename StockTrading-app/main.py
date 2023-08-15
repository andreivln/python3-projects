import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_ALPHA = os.environ['ALPHA_KEY']
API_KEY_NEWS = os.environ['NEWS_KEY']

ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_ALPHA
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yestarday_closing_price = yesterday_data["4. close"]
print(yestarday_closing_price)

# yesterday_close = data["Time Series (Daily)"]["2023-06-01"]["4. close"]
# print(yesterday_close)

data_before_yestarday_list = [value for (key2, value) in data.items()]
before_yestarday_data = data_before_yestarday_list[1]
before_yestarday_closing_price = before_yestarday_data["4. close"]
print(before_yestarday_closing_price)

x = float(yestarday_closing_price) - float(before_yestarday_closing_price)
up_down = None
if x > 0:
    up_down = '⬆'
else:
    up_down = '⬇'

print(x)

percentage_difference = round((x / float(yestarday_closing_price))) * 100
print(round(percentage_difference))


if abs(percentage_difference) == 0:
    parameters_news = {
        "q": COMPANY_NAME,
        "apiKey": API_KEY_NEWS,
        "title": COMPANY_NAME,
        "language": "en",
        "sortBy": "relevancy"
    }

    response_news = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    response_news.raise_for_status()
    data_news = response_news.json()["articles"]
    print(data_news)

    articles = data_news[0:3]
    print(articles)
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    print(formatted_articles)

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(body=article, from_="+13148977440", to='+40722733096')


        print(message.status)

