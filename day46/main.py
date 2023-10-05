import requests
from bs4 import BeautifulSoup
import lxml


travel_year = input(
    "Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")

response = requests.get(
    url=f"https://www.billboard.com/charts/hot-100/{travel_year}")
html_content = response.text

soup = BeautifulSoup(html_content, "lxml")
title_list = soup.select(selector="li", class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# print(title_list)
song_title_list = []

for title in title_list:
    song = title.getText()
    song_title_list.append(song)

print(song_title_list)
