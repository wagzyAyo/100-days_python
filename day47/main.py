from bs4 import BeautifulSoup
import requests
import lxml
import numpy


Product = "https://www.amazon.com/Beelink-SER5-Computer-Display-Bluetooth/dp/B0C3VJGWSL/ref=sr_1_1_sspa?crid=G9S4AW54HEY2&keywords=pc&qid=1696601812&sprefix=%2Caps%2C569&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A3OHI25ZCHSGMQ"

http_headers = {
    "Request": "LineGET / HTTP/1.1",
    "Host": "myhttpheader.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "_ga=GA1.2.541337992.1696594866; _gid=GA1.2.1609940826.1696594866; _ga_VL41109FEB=GS1.2.1696594868.1.0.1696594868.0.0.0",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "102.89.22.55"
}

response = requests.get(url=Product, headers=http_headers)
website = response.text

soup = BeautifulSoup(website, "lxml")
print(soup)


price_in_symbol = soup.select(selector="div span span", class_="a-offscreen")
price_list = [item.getText.split("$")[1] for item in price_in_symbol]

price = 0

for num in price_list:
    price = num

print(price)
