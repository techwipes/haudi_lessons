# -*- coding: utf-8 -*-
"""

script for getting weather info

"""

import pyowm

owm = pyowm.OWM('08ba5600a00017c0ee587931bfcfefa2')

city = input("What city do you wonna check?")

# Search for current weather in city 
observation = owm.weather_at_place(city)
w = observation.get_weather()
print(w)
