from bs4 import BeautifulSoup
import lxml


with open("day 45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

# print(soup.prettify())
# print(soup.title)
# print(soup.ul)
# print(soup.li)

tag_p = soup.find_all(name="p")
print(tag_p)

for tag in tag_p:
    print(tag.getText())
    print(tag.get("href"))


header = soup.find(name="h1", id="name")
print(header)

projects = soup.find(name="h3", class_="projects")
print(projects)
