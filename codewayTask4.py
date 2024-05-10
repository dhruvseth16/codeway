import requests
  
def get_weather_data(api_key, city_id):  
    api_url = "http://api.openweathermap.org/data/2.5/weather"  
    params = {  
        "id": city_id,  
        "units": "metric",  
        "appid": api_key  
    }  
    response = requests.get(api_url, params=params)  
    data = response.json()  
    return data  
  
api_key = "92c7efad3dc7c65580303c308c29e95b"  
city_id = "lat=23.0167, lon=76.7167"  # Moscow  
  
data = get_weather_data(api_key, city_id)  
print(data) 