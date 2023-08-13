import requests
from datetime import datetime
import os

# exemples " ran 3 miles " / " 30 min yoga" / "30 min weight lifting"

ENDPOINT = "https://trackapi.nutritionix.com"
APP_ID = os.environ["APP_ID_TRACKAPI"]
APP_KEY = os.environ["APP_KEY_TRACKAPI"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT_WORKOUT"]
TOKEN = os.environ["TOKEN_APITRACK"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

basic_header = {
    "Authorization": f"Basic {TOKEN}"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

nutrition_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 106,
    "height_cm": 180,
    "age": 24
}

response = requests.post(url=exercise_endpoint, json=nutrition_params, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%x")
now = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_input, headers=basic_header)

    print(sheet_response.text)

