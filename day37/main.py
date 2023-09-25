import requests

TOKEN = "giohieiq1903kdjjhdq1"
USER_NAME = "ayo79"

pixella_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixella_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixella_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}
Headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(graph_endpoint, json=graph_config, headers=Headers)
print(response.text)
