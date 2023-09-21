import requests
from datetime import datetime


MY_LAT = 9.081999
MY_LONG = 8.675277
API = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=API, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


time_now = datetime.now()
print(time_now.hour)

print(sunrise)
print(sunset)
