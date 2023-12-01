import urllib.request
import urllib.parse

with urllib.request.urlopen('http://pytholn.org') as response:
    html = response.read()