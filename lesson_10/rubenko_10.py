import sys

from prettytable import PrettyTable

import requests

import time

from constant import OPEN_WEATHER_API_KEY

x = PrettyTable()

weather_url = "http://api.openweathermap.org/data/2.5/weather"
forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"


### TASK ###
# input - take city name (Ukraine only) from user
# input mode - `current weather` or `forecast`
# show requested data with `pretty table` lib


weather_mode = {"0": "current_weather", "1": "forecast"}


def get_user_city_name() -> str:
    while True:
        city_name = input("Choose ukrainian city name: ")
        if not city_name.isalpha():
            print("You put wrong city name! Try once again.")
        else:
            break
    return city_name


def get_city_coord() -> dict:
    city_name = get_user_city_name()
    geocoding_params = {"q": city_name, 'appid': OPEN_WEATHER_API_KEY, "limit": 1}
    geocoding_res = requests.get(url=geocoding_url, params=geocoding_params)
    first = geocoding_res.json()[0]
    print(f"{city_name} = {first.get('country')}\n")
    try:
        if first.get('country') == "UA" or first.get('country') == "ua":
            city_coord = {"lat": first.get("lat"), "lon": first.get("lon")}
            print(f"{city_coord}\n")
            return city_coord
        else:
            print("You have put not ukrainian city!")
            sys.exit()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")


def get_weather_mode() -> str:
    while True:
        print("Choose weather mode you want to get:\n    0 - <<current weather>>\n    1 - <<forecast>>")
        mode = input()
        if mode == "0" or mode == "1":
            mode_status = weather_mode[mode]
            break
        else:
            print("You put wrong mode value! Try once again.")
    return mode_status


def get_weather_data(cnt_num: int):
    coord_data = get_city_coord()
    mode = get_weather_mode()
    if mode == "current_weather":
        weather_params = {"lat": coord_data["lat"], "lon": coord_data["lon"], "appid": OPEN_WEATHER_API_KEY,
                          "units": "metric"}
        weather_res = requests.get(url=weather_url, params=weather_params)
        raw_weather_data = weather_res.json()
        date = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(raw_weather_data.get("dt")))]
        some_data = raw_weather_data["main"]
        temperature = [str(some_data.get("temp"))]
        x.add_column("Weather date ", date)
        x.add_column("Temperature, *С", temperature)
        print(x)

    elif mode == "forecast":
        forecast_params = {"lat": coord_data["lat"], "lon": coord_data["lon"], "appid": OPEN_WEATHER_API_KEY,
                           "units": "metric", "cnt": cnt_num}
        forecast_res = requests.get(url=forecast_url, params=forecast_params)
        raw_forecast_data = forecast_res.json()
        some_data = raw_forecast_data.get("list")
        date_lis = []
        temp_list = []
        for el in range(0, cnt_num):
            date_lis.append(some_data[el].get("dt_txt"))
            for_raw_temperature_data_extraction = some_data[el].get("main")
            temp_list.append(for_raw_temperature_data_extraction["temp"])
        x.add_column("Forecast date and time", date_lis)
        x.add_column("Temperature, *С", temp_list)
        print(x)


get_weather_data(5)
