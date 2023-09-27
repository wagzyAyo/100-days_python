import requests
from datetime import datetime


API_ID = "392d7bf1"
API_KEY = "3ac8c95a4315c1b501d79d8817f0e7e4"


SHEETS_ENDPOINT = "https://api.sheety.co/1d155e4c8874acf4ebd5da8953b622ad/myWorkouts/workouts"

AUTH_SHEETY_HEADER = {
    "Authorization": "Bearer nodemodulator"
}

HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


API_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

msg = input("Tell me which excercise you did? ").title()

exercise_parameters = {
    "query": msg,
    "gender": "male"
}

response = requests.post(
    url=API_END_POINT, json=exercise_parameters, headers=HEADERS)
result = response.json()


today_date = datetime.now().strftime("%d/%m,%Y")
now_time = datetime.now().strftime("%X")

for item in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        }
    }
sheety_response = requests.post(
    url=SHEETS_ENDPOINT, json=sheet_inputs, headers=AUTH_SHEETY_HEADER)
print(sheety_response.text)
