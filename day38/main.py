import requests

HEADERS = {
    "APP_ID ": "392d7bf1",
    "API_KEY": "3ac8c95a4315c1b501d79d8817f0e7e4"
}

API_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

msg = input("Tell me which excercise you did? ")

exercise_parameters = {
    "query": msg,
    "gender": "male"
}

response = requests.post(
    url=API_END_POINT, params=exercise_parameters, headers=HEADERS)

print(response)
