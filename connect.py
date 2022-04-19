from unicodedata import name
import requests
import os
import json

with open('conf.json','r') as f:
    config = json.load(f)

api_key = config['api_key']
home = config['home']
aqi = config['include_aqi']
api_base_url = "http://api.weatherapi.com/v1/"
real_time_path = ""
forecast_path = ""

print(f"Home is {home}")
def get_real_time(query = home):
    """GET Real Time for requested location w/ air quality"""
    # Check if query/location is blank
    if query == "":
        print("No location given or found in conf.json")
        exit()
    elif query != "":
        real_time_path = f"{api_base_url}current.json?key={api_key}&q={query}&aqi={aqi}"

    r = requests.get(real_time_path).json()
    location_name = r['location']['name']
    temp = r['current']['temp_f']

    print(f"The current temperature in {location_name} is {temp}")



def get_forecast():
    """GET Forecast for requested location w/ number of days, air quality, alerts"""
    num_days = 5
    query = "91754"
    aqi = "no"
    alerts = "no"
    forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={query}&days={num_days}&aqi={aqi}&alerts={alerts}"


def get_astronomy():
    """GET Astronomical Data for requested location"""

