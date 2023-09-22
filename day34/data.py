import requests


parameters = {
    "amount": 10,
    "type": "boolean"
}
data = requests.get("https://opentdb.com/api.php", params=parameters)
data.raise_for_status()
question = data.json()
question_data = question["results"]
