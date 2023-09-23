import requests

open_waether = "https://api.openweathermap.org/data/2.5/weather"
API_key = "24be804efd2a6b236b7b470b07a85f69"
parameters = {
    "lat": 10,
    "lon": 8,
    "exclude": "current,minute,daily",
    "appid": API_key

}
will_rain = False

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
