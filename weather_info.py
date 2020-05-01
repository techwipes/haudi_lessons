# -*- coding: utf-8 -*-
"""

script for getting weather info

"""

import pyowm

owm = pyowm.OWM('08ba5600a00017c0ee587931bfcfefa2', language = "ru")

city = input("What city do you wonna check? ")

# Search for current weather in city 
observation = owm.weather_at_place(city)
w = observation.get_weather()

wind = w.get_wind()["speed"]                
humidity = w.get_humidity()            
temperature = w.get_temperature('celsius')["temp"]

print(" In city " + city + " " + w.get_detailed_status() + " now ")
print(" Temperature is: " + str(temperature) + u"\u00b0" + "C" )
print(" Wind is " + str(wind) + "m/s now ")
print(" Humidity is " + str(humidity) + "% now ")



