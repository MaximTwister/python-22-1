from pprint import pprint
import requests
import os
from prettytable import PrettyTable

weather_url = "https://api.openweathermap.org/data/2.5/weather"
geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
forecast_url = "http://api.openweathermap.org/data/2.5/forecast"

api_key = "33c5ec8515f15ff8ab32679ca9acda93"

# input - take city name (Ukraine only) from user
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
    res = requests.get(url=weather_url, params=params)
    try:
        res.raise_for_status()
        pprint(f"{weather_url} response:\n")
        pprint(res.json())
        return res.json().get("coord").values()
    except requests.exceptions.HTTPError:
        return None


def weather_city() -> dict:
    city = get_city()
    geocoding_params = {"q": city, "appid": api_key, "limit": 1}
    geocoding_res = requests.get(url=geocoding_url, params=geocoding_params)
    first_res: dict = dict(geocoding_res.json()[0])
    try:
        if first_res.get('country') == "UA" or first_res.get('country') == "ua":
            city_coordinates = {"lat": first_res.get("lat"), "lon": first_res.get("lon")}
            print(f"{city_coordinates}\n")
            return city_coordinates
        else:
            print("You have put not ukrainian city!")
    except:
        print("Error")


def get_city_f():
    while True:
        city = input("Enter your city and we will show you the weather "
                     "in that region:\n-> ")
        city_params = {"appid": api_key, "q": city}
        if get_city_forecast(city_params):
            return city
        else:
            print(f"\nUnfortunately we do not find your city: {city}\n"
                  f"Check your spell or try another city in that region.\n")


def get_city_forecast(params):
    res = requests.get(url=forecast_url, params=params)
    try:
        res.raise_for_status()
        pt = PrettyTable(["data", "temp", "temp_min", "temp_max", "humidity"])
        for l in res.json()["list"]:
            pt.add_row([l["dt_txt"],
                        l["main"]["temp"],
                        l["main"]["temp_min"],
                        l["main"]["temp_max"],
                        l["main"]["humidity"]])
        print(pt.get_string())
        return res.json()
    except requests.exceptions.HTTPError:
        return None


def forecast_city() -> dict:
    city = get_city_f()
    geocoding_params = {"q": city, "appid": api_key, "limit": 1}
    geocoding_res = requests.get(url=geocoding_url, params=geocoding_params)
    first_res: dict = dict(geocoding_res.json()[0])
    try:
        if first_res.get('country') == "UA" or first_res.get('country') == "ua":
            city_coordinates = {"lat": first_res.get("lat"), "lon": first_res.get("lon")}
            print(f"{city_coordinates}\n")
            return city_coordinates
        else:
            print("You have put not ukrainian city!")
    except:
        print("Error")


def main():
    while True:
        choice = input("Current weather or forecast: ")
        if choice == "weather":
            weather_city()
        elif choice == "forecast":
            forecast_city()
        elif choice == "0":
            pprint("End :)")
            break


main()
