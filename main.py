import random

import my_configuration
import requests
import json
from datetime import datetime

# 2 constants to store the APP_ID and APP_KEY that you got from Nutritionix.
NutritionixAppID = my_configuration.nutritionix_app_id
NutritionixAppKey = my_configuration.nutritionix_app_key


# Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for a plain text input.

# https://gist.github.com/mattsilv/9dfb709e7609537ffd3b1b8c097e9bfb
nutritionix_api_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

header = {
    "x-app-id": NutritionixAppID,
    "x-app-key": NutritionixAppKey
}

question = "for breakfast i ate 2 eggs, bacon, and french toast"
input_body = {
    "query": question,
    "timezone": "US/Eastern"
}

response = requests.post(url=nutritionix_api_url, headers=header, json=input_body)
#print(json.dumps(json.loads(response.text), indent=4))


exercise_that_i_did = f"{random.choice(['run', 'swim', 'jogging', 'walking'])} " \
                      f"{random.randint(1,10)} {random.choice(['kilos', 'miles'])} and " \
                      f"{random.choice(['lunges', 'push up', 'pull up', 'dumbbell rows', 'squat'])} for {random.randint(2,7)} minutes"
print(exercise_that_i_did)

GENDER = "MALE"
WEIGHT_KG = 79
HEIGHT_CM = 175
AGE = 32

nutritionix_api_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
input_body = {
    "query": exercise_that_i_did,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_api_url, headers=header, json=input_body)
parsed = json.loads(response.text)
result = response.json()

# Using the Sheety Documentation, write some code to use the Sheety API to generate a new row of data in your Google Sheet
# for each of the exercises that you get back from the Nutritionix API.
# The date and time columns should contain the current date and time from the Python datetime module.

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheet_endpoint = my_configuration.sheet_endpoint
sheet_token = my_configuration.sheet_token

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    bearer_headers = {
        "Authorization": f"Bearer {sheet_token}"
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)

