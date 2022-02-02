import requests
from datetime import datetime

api_key = "1ef9677a0b162641ee1daa1988395188"
# url variable composed of multiple variables
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# latitude and longitude of Bucharest
lat, lon = "44", "26"
complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key

# Cache responses so that we don't saturate the API
cache_time=0
cache_reset_timeout=5   # seconds
cache_response=None

def get_reference_temperature():
    global cache_time,cache_reset_timeout,cache_response
    x=None

    if datetime.now()-cache_time>cache_reset_timeout:
        cache_time=datetime.now()

        response = requests.get(complete_url)
        x = response.json()
        cache_response=x
    else:
        x=cache_response

    y = x["main"]
    current_temperature =round(y["temp"] - 273.15, 2) 
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    return current_temperature