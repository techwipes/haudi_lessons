# -*- coding: utf-8 -*-
"""

script for getting weather info

"""

import pyowm
from pyowm import exceptions


owm = pyowm.OWM('08ba5600a00017c0ee587931bfcfefa2', language = "ru")

city = input("What city do you wonna check? ")

# Search for current weather in city, with checking for wrong name of city
while True:
    try:
        observation = owm.weather_at_place(city)
        if type(str(observation)) == str:
            break
    except:
        print("Wrong City!")
        city = input("What city do you wonna check? ")


w = observation.get_weather()


wind = w.get_wind()["speed"]                
humidity = w.get_humidity()            
temperature = w.get_temperature('celsius')["temp"]
sunrise = w.get_sunrise_time('iso')  
sunset = w.get_sunset_time('iso')  

print("In city " + city + " " + w.get_detailed_status() + " now")
print("Temperature is: " + str(temperature) + u"\u00b0" + "C")
print("Wind is " + str(wind) + "m/s now")
print("Humidity is " + str(humidity) + "% now")
print("The sun rises in " + sunrise)
print("The sun sets in " + sunset)


if temperature < 10:
    print("It's cold outside, dress in warm clothes")
elif temperature < 20:
    print("It's warm outside, dress easy")
else:
    print("It's very warm outside, enjoy!")
