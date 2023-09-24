import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


API_KEY = "H1R6T6GE7NUG1FHC"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "94388d43ec994d8b899f4444156e73a3"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

data = requests.get(STOCK_ENDPOINT, params=parameters)
data.raise_for_status()
stock_data = data.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


day_before_yesterday = data_list[1]
day_before_yesterday_close = day_before_yesterday["4. close"]
print(day_before_yesterday_close)

difference_in_stock_price = abs(float(
    yesterday_closing_price) - float(day_before_yesterday_close))

print(difference_in_stock_price)

diff_percent = (difference_in_stock_price /
                float(day_before_yesterday_close)) * 100
print(diff_percent)


new_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
if diff_percent > 3:
    response = requests.get(NEWS_ENDPOINT, params=new_params)
    response.raise_for_status()
    new_data = response.json()["articles"]
    three_articles = new_data[:3]
    print(three_articles)
