import requests
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
alerts = config['include_alerts']
use_metric = config['use_metric']
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
        conditions = r['current']['condition']
        condition = conditions['text']
        uv = r['current']['uv']
        humidity = str(f"{r['current']['humidity']}%")
        if use_metric:            
            temp = str(f"{r['current']['temp_c']} °C")
            total_precip = str(f"{r['current']['precip_mm']} mm")
        elif not use_metric:
            temp = str(f"{r['current']['temp_f']} °F")
            total_precip = str(f"{r['current']['precip_in']} in")

    # Format
    print(f"Current Weather in {location_name}")
    print(f"Temp: {temp}")
    print(f'Condition: {condition}')
    print(f'Humidity: {humidity}')
    print(f'UV Index: {uv}')
    print(f"Rain total: {total_precip}")

def get_today(query: str = typer.Argument(None)):
    """GET today's weather"""
    # Check if query/location is blank
    if query is None and home is None:
        print("No location given or found in conf.json")
        exit()
    elif query is not None:
        forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={query}&days=1&aqi={aqi}&alerts={alerts}"
    elif query is None and home is not None:
        forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={home}&days=1&aqi={aqi}&alerts={alerts}"

    # Pull from API Endpoint
    try:
        r = requests.get(forecast_path).json()
    except:
        print("API Error")
    else:
        forecast = r['forecast']['forecastday']
        location_name = r['location']['name']
        condition = r['current']['condition']['text']
        humidity = str(f"{forecast[0]['day']['avghumidity']}%")
        uv = r['current']['uv']
        if use_metric:
            curr_temp = str(f"{r['current']['temp_c']}°C")
            max_temp = str(f"{forecast[0]['day']['maxtemp_c']}°C")
            min_temp = str(f"{forecast[0]['day']['mintemp_c']}°C") 
            avg_temp =  str(f"{forecast[0]['day']['avgtemp_c']}°C")
            total_precip = str(f"{forecast[0]['day']['totalprecip_mm']} mm")
        elif not use_metric:
            curr_temp = str(f"{r['current']['temp_f']} °F")
            max_temp = str(f"{forecast[0]['day']['maxtemp_f']}°F")
            min_temp = str(f"{forecast[0]['day']['mintemp_f']}°F") 
            avg_temp =  str(f"{forecast[0]['day']['avgtemp_f']}°F")
            total_precip = str(f"{forecast[0]['day']['totalprecip_in']} in")

    # Format
    print(f"It will be {condition} in {location_name} today")
    print(f"Humidity will average {humidity}, the UV index is {uv}")
    print(f"You can expect {total_precip} of rain")
    print(f"Current Temp: {curr_temp}, Avg Temp: {avg_temp}")
    print(f"Max Temp:     {max_temp}, Min Temp: {min_temp}")
  
def get_forecast(query: str = typer.Argument(None), num_days = 5) -> None:
    """GET Forecast for requested location w/ number of days, air quality, alerts""" 
    # Check if query/location is blank
    if query is None and home is None:
        print("No location given or found in conf.json")
        exit()
    elif query is not None:
        forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={query}&days=1&aqi={aqi}&alerts={alerts}"
    elif query is None and home is not None:
        forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={home}&days=1&aqi={aqi}&alerts={alerts}"

    # Pull from API Endpoint
    try:
        r = requests.get(forecast_path).json()
    except:
        print("API Error")
    else:
        # iterate days
        location_name = r['location']['name']
        for day in num_days:
            forecast = r['forecast']['forecastday']            
            condition = r['current']['condition']['text']
            humidity = str(f"{forecast[day]['day']['avghumidity']}%")
            uv = r['current']['uv']
            if use_metric:
                curr_temp = str(f"{r['current']['temp_c']}°C")
                max_temp = str(f"{forecast[day]['day']['maxtemp_c']}°C")
                min_temp = str(f"{forecast[day]['day']['mintemp_c']}°C") 
                avg_temp =  str(f"{forecast[day]['day']['avgtemp_c']}°C")
                total_precip = str(f"{forecast[day]['day']['totalprecip_mm']} mm")
            elif not use_metric:
                curr_temp = str(f"{r['current']['temp_f']} °F")
                max_temp = str(f"{forecast[day]['day']['maxtemp_f']}°F")
                min_temp = str(f"{forecast[day]['day']['mintemp_f']}°F") 
                avg_temp =  str(f"{forecast[day]['day']['avgtemp_f']}°F")
                total_precip = str(f"{forecast[day]['day']['totalprecip_in']} in")

            # Format
            print(f"Day {day + 1}")
            print(f"You can expect {total_precip} of rain")
            """ print(f"It will be {condition} in {location_name} today")
            print(f"Humidity will average {humidity}, the UV index is {uv}")
            print(f"You can expect {total_precip} of rain")
            print(f"Current Temp: {curr_temp}, Avg Temp: {avg_temp}")
            print(f"Max Temp:     {max_temp}, Min Temp: {min_temp}") """

def get_astronomy():
    """GET Astronomical Data for requested location"""
