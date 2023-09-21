import requests
from datetime import datetime
import smtplib
import ssl
import time

EMAIL = "talktojmcvibes@gmail.com"
PASSWORD = "*************"

MY_LAT = 9.081999
MY_LONG = 8.675277
API = "https://api.sunrise-sunset.org/json"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longtitude = float(data["iss_position"]['longitude'])
    iss_latitude = float(data["iss_position"]["latitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longtitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url=API, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
# And it is currently dark
# Then send me an email


context = ssl.create_default_context()  # Adds layer of security
while True:
    if is_iss_overhead() and is_night():
        time.sleep(60)
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="jmcvibes@yahoo.com",
                msg="Subject:Look Up\n\nThe ISS is above you in the sky."
            )
