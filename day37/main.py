import requests

pixella_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "giohieiq1903kdjjhdq1",
    "username": "ayo79",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixella_endpoint, json=user_params)
print(response.text)
