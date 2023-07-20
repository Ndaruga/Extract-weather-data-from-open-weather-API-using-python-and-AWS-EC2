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
print(data)
