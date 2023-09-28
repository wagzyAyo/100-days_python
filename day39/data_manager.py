import requests
from pprint import pprint
SHEETY_API_ENDPOINT = "https://api.sheety.co/1d155e4c8874acf4ebd5da8953b622ad/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        self.response = requests.get(url=SHEETY_API_ENDPOINT)
        self.data = self.response.json()
        self.formated_data = self.data["prices"]
        return self.formated_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
