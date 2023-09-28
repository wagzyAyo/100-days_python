import requests
from pprint import pprint
SHEETY_API_ENDPOINT = "https://api.sheety.co/1d155e4c8874acf4ebd5da8953b622ad/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_destination_data = {}

    def get_destination_data(self):
        self.response = requests.get(url=SHEETY_API_ENDPOINT)
        self.data = self.response.json()
        self.formated_data = self.data["prices"]
        return self.formated_data
