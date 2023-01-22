from pprint import pprint
from prettytable import PrettyTable
from constants import (
    OPEN_WEATHER_API_KEY,
    TABLE_TITLES,
)

import requests


weather_url = "http://api.openweathermap.org/data/2.5/weather"
forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
# geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"


# Optionally we can use geocoding to get city coordinates (lat, lon).
#
# geocoding_params = {"q": "Dnipro", "appid": OPEN_WEATHER_API_KEY, "limit": 1}
# geocoding_res = requests.get(url=geocoding_url, params=geocoding_params)
# first_res: dict = geocoding_res.json()[0]
# city_coordinates = {"lat": first_res.get("lat"), "lon": first_res.get("lon")}

weather_params = {"q": "Dnipro", "appid": OPEN_WEATHER_API_KEY, "limit": 1}
weather_res = {}
city = input("Enter the city name (Ukraine only): ")
mode = input("Select mode - 'c for `current weather` or 'f' for `forecast`: ")

if city and mode == "c":
    weather_params["q"] = city
    weather_res = requests.get(url=weather_url, params=weather_params)
    pprint(weather_res.json())
elif city and mode == "f":
    weather_params["q"] = city
    weather_res = requests.get(url=forecast_url, params=weather_params)
    pprint(weather_res.json())
else:
    print("Data isn`t correct")

# in constants.py TABLE_TITLES = ["q", "temp", "pressure", "wind", "clouds"]
# pt = PrettyTable(TABLE_TITLES)
# for day in weather_res:
#    pt.add_row([day.get(key) for key in TABLE_TITLES])
# print(pt.get_string(fields=TABLE_TITLES))