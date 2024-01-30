import datetime as dt
import requests
from randomCity import get_random_capital_city
from randomCity import capital_city

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()
CITY = capital_city

def kelvinToCelsiusFahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahreheit =  kelvinToCelsiusFahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_farenheit = kelvinToCelsiusFahrenheit(feels_like_kelvin)
windspeed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

#print(response)
print(f"Temperature in {CITY}: {temp_celsius:.2f}")
