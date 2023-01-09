from pprint import pprint

import requests
from constant import OPEN_WEATHER_API_KEY

weather_url = "http://api.openweathermap.org/data/2.5/weather"
geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"

# Optionally we can use geocoding to get city coordinates (lat, lon).
#
# geocoding_params = {"q": "Dnipro", "appid": OPEN_WEATHER_API_KEY, "limit": 1}
# geocoding_res = requests.get(url=geocoding_url, params=geocoding_params)
# first_res: dict = geocoding_res.json()[0]
# city_coordinates = {"lat": first_res.get("lat"), "lon": first_res.get("lon")}

weather_params = {}
weather_res = requests.get(url=weather_url, params=weather_params)
pprint(weather_res.json())

### TASK ###
# input - take city name (Ukraine only) from user
# input mode - `current weather` or `forecast`
# show requested data with `pretty table` lib
