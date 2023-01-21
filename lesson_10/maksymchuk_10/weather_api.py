from pprint import pprint
import requests
from tabulate import tabulate
import os


api_key = os.environ["OPEN_WEATHER_API_KEY"]
weather_ep = "https://api.openweathermap.org/data/2.5/weather"
circle_ep = "https://api.openweathermap.org/data/2.5/find"

def get_city():
    while True:
        city = input("Enter your city and we will show you the weather "
                     "in that region:\n-> ")
        city_params = {"appid": api_key, "q": city}
        if get_city_coord(city_params):
            return city
        else:
            print(f"\nUnfortunately we do not find your city: {city}\n"
                  f"Check your spell or try another city in that region.\n")


def get_city_coord(params):
    res = requests.get(url=weather_ep, params=params)
    try:
        res.raise_for_status()
        pprint(f"{weather_ep} response:\n{res.json()}")
        return res.json().get("coord").values()  # 34.9833, 48.45
    except requests.exceptions.HTTPError:
        return None


def get_near_cities_weather(params):
    res = requests.get(url=circle_ep, params=params)
    pprint(f"Circle find results: {res.json()}")
    return res.json().get("list")


def get_weather_ico(weather: dict):
    ico_dict = {
        "2**": '⛈️',
        "3**": '🌧️',
        "5**": '☔️',
        "6**": '❄️',
        "7**": '🌫️',
        "800": '☀️',
        "8**": '🌥️',
    }
    descr = weather.get("description")
    specific_id = str(weather.get("id"))  # Only 800
    ico = ico_dict.get(specific_id)
    if not ico:
        general_id = f"{specific_id[0]}**"
        ico = ico_dict.get(general_id)

    return f"{descr} {ico}"


def get_weather_data(city):
    city_name = city.get("name")

    weather_dict = city.get("weather")[0]
    weather_ico = get_weather_ico(weather_dict)

    main_dict = city.get("main")
    main_data = [main_dict.get(el) for el in ["temp", "temp_min", "temp_max", "pressure", "humidity"]]

    return [city_name, weather_ico, *main_data]


def main():
    city = get_city()  # Dnipro

    city_params = {"appid": api_key, "q": city}
    lon, lat = get_city_coord(city_params)

    circle_params = {
        "appid": api_key,
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "cnt": 5
    }
    cities_weather_list = get_near_cities_weather(circle_params)

    headers = ["City", "Sky", "Current Temp [℃]", "Min Temp [℃]", "Max Temp [℃]", "Pressure [hPa]", "Humidity [%]"]
    table_body = map(get_weather_data, cities_weather_list)
    print(tabulate(
        tabular_data=table_body,
        headers=headers,
        tablefmt="fancy_grid",
        numalign="center",
        stralign="center",
    ))

main()
