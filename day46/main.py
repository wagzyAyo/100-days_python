import requests
from bs4 import BeautifulSoup
import lxml


travel_year = input(
    "Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")

response = requests.get(
    url=f"https://www.billboard.com/charts/hot-100/{travel_year}")
html_content = response.text

soup = BeautifulSoup(html_content, "lxml")
title_list = soup.select(selector="li ul li h3")
# print(title_list)
song_title_list = [title.getText().strip() for title in title_list]

print(song_title_list)
