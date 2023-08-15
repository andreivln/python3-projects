import requests
from pprint import pprint
import os

SHEET_API_ENDPOINT = "https://api.sheety.co/be82924dcec55363d7118714b006609a/flightDealsAndrei/prices"
BEARER = os.environ['BEARER']

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json"
}



class DataManager:
  


    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
      
        response = requests.get(url=SHEET_API_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]

   
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_API_ENDPOINT}/{city['id']}",
                headers=headers,
                json=new_data
            )
            print(response.text)
