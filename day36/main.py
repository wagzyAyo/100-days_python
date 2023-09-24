import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


API_KEY = "H1R6T6GE7NUG1FHC"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everyrhing"

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

difference_in_stock_price = float(
    day_before_yesterday_close) - float(yesterday_closing_price)

print(difference_in_stock_price)
