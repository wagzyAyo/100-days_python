import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get("https://opentdb.com/api.php", params=parameters)
data.raise_for_status()

questions = data.json()
questions_data = questions["results"]
print(questions_data)
