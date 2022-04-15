import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')
api_base_url = "http://api.weatherapi.com/v1/"


def get_real_time():
    """GET Real Time for requested location w/ air quality"""
    query = "91754"
    aqi = "no"
    real_time_path = f"{api_base_url}current.json?key={api_key}&q={query}&aqi={aqi}"

    r = requests.get(real_time_path)
    print(r.status_code)
    print(r.text)


def get_forecast():
    """GET Forecast for requested location w/ number of days, air quality, alerts"""
    num_days = 5
    query = "91754"
    aqi = "no"
    alerts = "no"
    forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={query}&days={num_days}&aqi={aqi}&alerts={alerts}"


def get_astronomy():
    """GET Astronomical Data for requested location"""


get_real_time()
