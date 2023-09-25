import requests
from datetime import datetime

TOKEN = "giohieiq1903kdjjhdq1"
USER_NAME = "ayo79"
GRAPH1 = "graph1"


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
# response = requests.post(graph_endpoint, json=graph_config, headers=Headers)
# print(response.text)

today = datetime(year=2023, month=8, day=7)


pixel_endpoint = f"{pixella_endpoint}/{USER_NAME}/graphs/{GRAPH1}"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "45.9"
}
print(pixel_params["date"])

response = requests.post(
    url=pixel_endpoint, json=pixel_params, headers=Headers)
print(response.text)
