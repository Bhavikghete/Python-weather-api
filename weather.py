import requests
from requests import api

from dotenv import load_dotenv

load_dotenv()

import os


location = input("Enter the location : ")

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+os.getenv("userapi")

api_link = requests.get(complete_api_link)
api_data = api_link.json()


if api_data['cod'] == '404' :
   print("Invalid City Name {} - plz check the city name".format(location))

else:

    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']

    print("Weather Stats For : {}".format(location.upper()))
    print("Current Temperature is: {:.2f} deg C".format(temp_city))
    print("Weather desc :",weather_desc)
    print("Current Humidity :",hmdt, '%')
    print("Current Wind Speed :",wind_spd)



