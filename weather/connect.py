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
epa_grades = {
    1:"Good",
    2:"Moderate",
    3:"Unhealthy for sensitive groups",
    4:"Unhealthy",
    5:"Very Unhealthy",
    6:"Hazardous"
}

# function to make all API calls
def call_current(query: str = typer.Argument(None)):
    """GET current weather"""
    # Check if query/location is blank
    if query is None and home is None:
        print("No location given or found in conf.json")
        exit()
    elif query is not None:
        real_time_path = f"{api_base_url}current.json?key={api_key}&q={query}&aqi={aqi}"
    elif query is None and home is not None:
        real_time_path = f"{api_base_url}current.json?key={api_key}&q={home}&aqi={aqi}"

    try:
        r = requests.get(real_time_path).json()
    except:
        print("API Error")

    return r

def call_forecast(query: str, num_days: int):
    """GET today's weather"""
    # Check if query/location is blank
    if query is None and home is None:
        print("No location given or found in conf.json")
        exit()
    elif query is not None:
        forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={query}&days={num_days}&aqi={aqi}&alerts={alerts}"
    elif query is None and home is not None:
        forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={home}&days={num_days}&aqi={aqi}&alerts={alerts}"

    # Pull from API Endpoint
    try:
        r = requests.get(forecast_path).json()
    except:
        print("API Error")

    return r

def get_now(query: str = typer.Argument(None)):
    # Call necessary API function
    r = call_current(query)
    
    location_name = r['location']['name']
    condition = r['current']['condition']['text']
    uv = r['current']['uv']
    humidity = str(f"{r['current']['humidity']}%")
    if use_metric:            
        temp = str(f"{r['current']['temp_c']} ??C")
        total_precip = str(f"{r['current']['precip_mm']} mm")
    elif not use_metric:
        temp = str(f"{r['current']['temp_f']} ??F")
        total_precip = str(f"{r['current']['precip_in']} in")
    if aqi:
        airqual = r["current"]["air_quality"]["us-epa-index"]


    # Format Output
    print(f"Current Weather in {location_name}")
    print(f"Temp: {temp}")
    print(f'Condition: {condition}')
    print(f'Humidity: {humidity}')
    print(f'UV Index: {uv}')
    print(f"Rain total: {total_precip}")
    print(f"Air quality is {epa_grades[airqual]} ")

def get_today(query: str = typer.Argument(None)):
    # Call necessary API function
    r = call_forecast(query, 1)

    forecast = r["forecast"]["forecastday"]
    location_name = r['location']['name']
    condition = r['current']['condition']['text']
    humidity = str(f"{forecast[0]['day']['avghumidity']}%")
    uv = r['current']['uv']
    if use_metric:
        curr_temp = str(f"{r['current']['temp_c']}??C")
        max_temp = str(f"{forecast[0]['day']['maxtemp_c']}??C")
        min_temp = str(f"{forecast[0]['day']['mintemp_c']}??C") 
        avg_temp =  str(f"{forecast[0]['day']['avgtemp_c']}??C")
        total_precip = str(f"{forecast[0]['day']['totalprecip_mm']} mm")
    elif not use_metric:
        curr_temp = str(f"{r['current']['temp_f']} ??F")
        max_temp = str(f"{forecast[0]['day']['maxtemp_f']}??F")
        min_temp = str(f"{forecast[0]['day']['mintemp_f']}??F") 
        avg_temp =  str(f"{forecast[0]['day']['avgtemp_f']}??F")
        total_precip = str(f"{forecast[0]['day']['totalprecip_in']} in")

    # Format
    print(f"{location_name} will be {condition} with {total_precip} of rain")
    print(f"Humidity: {humidity} UV index: {uv}")
    print(f"Curr    : {curr_temp},   Avg : {avg_temp}")
    print(f"High    : {max_temp},   Low : {min_temp}")
  
def get_forecast(query: str = typer.Argument(None), num_days = None):
    num_days = int(num_days)
    if num_days is None:
        num_days = 3
    elif num_days > 3:
        print("Maximum forecast length is 3 days")
        num_days = 3
    # Call necessary API function
    r = call_forecast(query, num_days)
    # grab entire forecast
    entire_forecast = r["forecast"]['forecastday']

    location_name = r['location']['name']
    # iterate days
    for day in range(0,num_days):
        condition = entire_forecast[day]['day']['condition']['text']
        humidity = str(f"{entire_forecast[day]['day']['avghumidity']}%")
        uv = r['current']['uv']
        if use_metric:
            curr_temp = str(f"{r['current']['temp_c']}??C")
            max_temp = str(f"{entire_forecast[day]['day']['maxtemp_c']}??C")
            min_temp = str(f"{entire_forecast[day]['day']['mintemp_c']}??C") 
            avg_temp =  str(f"{entire_forecast[day]['day']['avgtemp_c']}??C")
            total_precip = str(f"{entire_forecast[day]['day']['totalprecip_mm']} mm")
        elif not use_metric:
            curr_temp = str(f"{r['current']['temp_f']} ??F")
            max_temp = str(f"{entire_forecast[day]['day']['maxtemp_f']}??F")
            min_temp = str(f"{entire_forecast[day]['day']['mintemp_f']}??F") 
            avg_temp =  str(f"{entire_forecast[day]['day']['avgtemp_f']}??F")
            total_precip = str(f"{entire_forecast[day]['day']['totalprecip_in']} in")

        # Format
        print(f"Day {day + 1}")
        print(f"{location_name} will be {condition} with {total_precip} of rain")
        print(f"Humidity: {humidity} UV index: {uv}")
        print(f"Curr    : {curr_temp},   Avg : {avg_temp}")
        print(f"High    : {max_temp},   Low : {min_temp}")

def get_astronomy():
    """GET Astronomical Data for requested location"""

