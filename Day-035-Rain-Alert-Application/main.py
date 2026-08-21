import requests
import os

api_key = os.environ.get("OWN_API_KEY") #Your API KEY
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 24.860735,
    "lon": 67.001137,
    "cnt" : 4,
    "appid" : api_key,
}

response = requests.get(url= OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")