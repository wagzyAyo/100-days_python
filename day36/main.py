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
print(data_list)
