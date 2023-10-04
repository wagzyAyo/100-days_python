import requests
from bs4 import BeautifulSoup
import lxml

empire_site = requests.get(
    url="https://www.empireonline.com/movies/features/best-movies-2/")

site_content = empire_site.text

soup = BeautifulSoup(site_content, "lxml")
title = soup.select(
    selector="h3", class_="listicleItem_listicle-item__title__hW_Kn")

film_title = [text.getText() for text in title]

print(film_title)
