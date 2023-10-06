import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOT_ID = "feadbc8159364400a48a91f26e1fe9bd"
SECRETE = "c6eeaef8cf86429e842e58735eda534d"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=SPOT_ID,
        client_secret=SECRETE,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]


travel_year = input(
    "Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")

response = requests.get(
    url=f"https://www.billboard.com/charts/hot-100/{travel_year}")
html_content = response.text

soup = BeautifulSoup(html_content, "lxml")
title_list = soup.select(selector="li ul li h3")
# print(title_list)
song_title_list = [title.getText().strip() for title in title_list]

# print(song_title_list)

song_uris = []

year = travel_year.split("-")[0]
for song in song_title_list:
    result = sp.search(q=f"track:{song} year={year}", type='track')
    print(result)
    try:
        uri = result["tracks"]['items'][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped")


# print(song_uris)

playlist = sp.user_playlist_create(
    user=user_id, name=f"{travel_year} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
