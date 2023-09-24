import requests
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

EMAIL = "talktojmcvibes@gmail.com"
PASSWORD = "******************"
context = ssl.create_default_context()

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
    formated_article = [
        f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = "jmcvibes@yahoo.com"
    msg['Subject'] = f"{COMPANY_NAME} update"

    # Add each formatted article as a text part to the message
    for article_text in formated_article:
        part = MIMEText(article_text, 'plain')
        msg.attach(part)
        # Convert the message to a string
        message = msg.as_string()

        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as mail:
            mail.login(user=EMAIL, password=PASSWORD)
            mail.sendmail(from_addr=EMAIL,
                          to_addrs="jmcvibes@yahoo.com", msg=message)
