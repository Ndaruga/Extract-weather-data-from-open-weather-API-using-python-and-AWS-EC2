import json
from datetime import datetime
import pandas as pd
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='

with open("api_key", 'r') as f:
    API_KEY = f.read()


city_name = input("Enter city name: ")

if not city_name:
    print("Invalid city name")
else:
    URL = BASE_URL + city_name + "&appid="+API_KEY

req = requests.get(URL)
data = req.json()

# -------------------------------------------------------

def get_all_json_keys(json_data):
    """Get all JSON keys in a JSON object.

    Args:
        json_data (dict): The JSON object to get the keys from.

    Returns:
        list: A list of all the JSON keys.
    """

    keys = []
    for key, value in json_data.items():
        if isinstance(value, dict):
            keys += get_all_json_keys(value)
        elif isinstance(value, list):
            for item in value:
                keys += get_all_json_keys(item)
        else:
            keys.append(key)
    return keys

keys = get_all_json_keys(data)
print(keys)