from operator import truediv
from unicodedata import name
import requests
import os
import json
import typer

try:
    with open('conf.json','r') as f:
        config = json.load(f)
except:
    print("Could not load conf.json")

api_key = config['api_key']
home = config['home']
aqi = config['include_aqi']
api_base_url = "http://api.weatherapi.com/v1/"
real_time_path = ""
forecast_path = ""

def get_now(query: str = typer.Argument(None)):
    """GET current weather"""
    # Check if query/location is blank
    if query is None and home is None:
        print("No location given or found in conf.json")
        exit()
    elif query is not None:
        real_time_path = f"{api_base_url}current.json?key={api_key}&q={query}&aqi={aqi}"
    elif query is None and home is not None:
        real_time_path = f"{api_base_url}current.json?key={api_key}&q={home}&aqi={aqi}"

    # Pull from API Endpoint
    try:
        r = requests.get(real_time_path).json()
    except:
        print("API Error")
    else:
        location_name = r['location']['name']
        temp = r['current']['temp_f']

    # Format
    print(f"{location_name}")
    print(f"Current Temp: {temp} in {location_name}")

def get_real_time(query = home):
    """GET Real Time for requested location w/ air quality"""
    # Check if query/location is blank
    if query == "":
        print("No location given or found in conf.json")
        exit()
    elif query != "":
        real_time_path = f"{api_base_url}current.json?key={api_key}&q={query}&aqi={aqi}"

    # Pull from API Endpoint
    try:
        r = requests.get(real_time_path).json()
    except:
        print("API Error")
    else:
        location_name = r['location']['name']
        temp = r['current']['temp_f']

    # Format
    print(f"The current temperature in {location_name} is {temp}")

def get_forecast(query = home, num_days = 5):
    """GET Forecast for requested location w/ number of days, air quality, alerts""" 
    aqi = "no"
    alerts = "no"
    forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={query}&days={num_days}&aqi={aqi}&alerts={alerts}"

def get_astronomy():
    """GET Astronomical Data for requested location"""

