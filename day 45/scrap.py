from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://www.ycombinator.com")

site = response.text

soup = BeautifulSoup(site, "lxml")
print(soup.title)
