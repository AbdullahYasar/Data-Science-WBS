
import datetime 
import requests 
from pprint import pprint

lat = 52.5244
lon = 13.4105
city_name = "Berlin"
country_code = "de"

api_key = "bf74a3d336b9f22dd6af67b521a73839"
units = "metric"
lang = "de"


# Using lat, lon
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}&lang={lang}"

# Using city name and country code
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units={units}&lang={lang}"



# 1. Get the REposne of the request
response = requests.get(URL)


print(response) # HTTP Repspone code 

data = response.json()

pprint(data)


print(data["name"]) # Berlin

print(data["main"]["temp"])
print(data["weather"][0]["description"])



sunrise = data["sys"]["sunrise"]
sunset = data["sys"]["sunset"]


# UTC
sunrise = datetime.datetime.utcfromtimestamp(sunrise)
sunset = datetime.datetime.utcfromtimestamp(sunset)

print(sunrise)
print(sunset)




