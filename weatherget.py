# openweathermap.org
# pypi.org
#pip install pyowm
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')#, {Language:"ru"})
mgr = owm.weather_manager()
#place = 'London,GB'
#place = input('ENTER city:')
place = 'Minsk,BY'
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather
#print(w)
print('city:', place)
print('detailed_status:', w.detailed_status)     # 'clouds'
print('wind:', w.wind())                         # {'speed': 4.6, 'deg': 330}
print('humidity:', w.humidity)                   # 87
print('temperature:', w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print('tC cur:', w.temperature('celsius')['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print('rain"', w.rain)                           # {}
print('heat_index:', w.heat_index)               # None
print('clouds:', w.clouds)                       #  75

