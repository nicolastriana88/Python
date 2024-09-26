import requests
from pprint import pprint 

API_Key = '63f99f94a9f19e2249342e4a59c22131'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key +" &=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)  