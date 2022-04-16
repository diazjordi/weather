api_base_url = "http://api.weatherapi.com/v1/"
real_time_path = f"{api_base_url}current.json?key={api_key}&q={query}&aqi={aqi}"
forecast_path = f"{api_base_url}forecast.json?key={api_key}&q={query}&days={num_days}&aqi={aqi}&alerts={alerts}"
