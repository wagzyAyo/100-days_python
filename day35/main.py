import requests

open_waether = "https://api.openweathermap.org/data/2.5/weather"
API_key = "24be804efd2a6b236b7b470b07a85f69"
parameters = {
    "lat": 10,
    "lon": 8,
    "appid": API_key
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather", params=parameters)
data = response.json()
print(data)
