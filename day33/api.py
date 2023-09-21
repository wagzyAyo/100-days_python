import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

is_longtitude = data["iss_position"]['longitude']
is_latitude = data["iss_position"]["latitude"]
position = (is_longtitude, is_latitude)
print(position)
