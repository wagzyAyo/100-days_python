import urllib.request
import urllib.parse

response = urllib.request.urlopen('http://python.org/')
html = response.read()