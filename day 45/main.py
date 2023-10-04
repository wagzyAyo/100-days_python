from bs4 import BeautifulSoup
import lxml


with open("day 45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

# print(soup.prettify())
# print(soup.title)
# print(soup.ul)
# print(soup.li)
