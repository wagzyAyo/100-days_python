import requests
from datetime import datetime

API_ID = "392d7bf1"
API_KEY = "3ac8c95a4315c1b501d79d8817f0e7e4"

HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

SHEETY_ENDPOINT = "https://api.sheety.co"

API_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

msg = input("Tell me which excercise you did? ").title()

exercise_parameters = {
    "query": msg,
    "gender": "male"
}

response = requests.post(
    url=API_END_POINT, json=exercise_parameters, headers=HEADERS)
result = response.json()

length = len(result['exercises'])
print(length)

print(result)

new_data = []


for item, value in result.items():
    count = 0
    if count > len(result):
        break

    user_input = result[item][count]
    user_activity = user_input["user_input"]
    work_out_duration = user_input['duration_min']
    calories_burn = user_input['nf_calories']
    count + 1
    date = datetime.now().strftime("%d/%m/%Y")
    new_data.append([date, user_activity, work_out_duration, calories_burn])


print(new_data)
