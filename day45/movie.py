import requests
from bs4 import BeautifulSoup
import lxml
import re

empire_site = requests.get(
    url="https://www.empireonline.com/movies/features/best-movies-2/")

site_content = empire_site.text

soup = BeautifulSoup(site_content, "lxml")
title = soup.select(
    selector="h3", class_="listicleItem_listicle-item__title__hW_Kn")

film_title = [text.getText() for text in title]

# print(film_title)

movie_list = []
number = 1
for film in film_title:
    splited = film.split(')')
    movie_title = splited[1]
    # print(f"{number}) {movie_title}")
    movie = f"{number}) {movie_title}"
    movie_list.append(movie)
    number += 1

for movie in movie_list:
    with open(file="day45/movies.txt", mode='a') as file:
        file.write(f"{movie}\n")
