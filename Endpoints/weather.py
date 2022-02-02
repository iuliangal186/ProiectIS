"""
Weather API documentation can be found here: https://openweathermap.org/current
The api_key is from the account that I made (Staicu Bogdan), I don't think the key will change anytime soon.
"""

import requests, json
from flask import (
    Blueprint, request, jsonify
)

from common import root_topic

sensor_root_topic = "weather"
bp = Blueprint("weather", __name__, url_prefix="/weather")


@bp.route("/", methods=["GET"])
def handler_get():
    # No new event was found so trigger a new one
    # API key
    api_key = "1ef9677a0b162641ee1daa1988395188"

    # url variable composed of multiple variables
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # latitude and longitude of Bucharest
    lat, lon = "44", "26"
    complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key

    response = requests.get(complete_url)

    x = response.json()
    y = x["main"]

    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    # print following values
    # print(" Temperature (in celsius) = " + str(round(current_temperature - 273.15, 2)))

    return jsonify({
        "status": "API succesfully read",
        "data": " Temperature (in celsius) = " + str(round(current_temperature - 273.15, 2))
    })


"""
print(" Temperature (in celsius) = " +
      str(round(current_temperature - 273.15, 2)) +
      "\n atmospheric pressure (in hPa unit) = " +
      str(current_pressure) +
      "\n humidity (in percentage) = " +
      str(current_humidity) +
      "\n description = " +
      str(weather_description))
"""

def mqtt_on_message(client,userdata,msg):
    sensor_topic=root_topic+sensor_root_topic
    if not sensor_topic==msg.topic:
        return

    print(f"Outside temperature: received {msg.payload.decode()} from {msg.topic} topic")

    json_msg=json.loads(msg.payload.decode())
