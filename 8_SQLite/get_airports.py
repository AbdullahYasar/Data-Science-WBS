import requests
from pprint import pprint

url = "https://aerodatabox.p.rapidapi.com/airports/search/location"

querystring = {"lat":"52.5244","lon":"13.4105","radiusKm":"50","limit":"10","withFlightInfoOnly":"false"}

headers = {
	"X-RapidAPI-Key": "57e40df905msh89f91a584028707p1724bfjsn063fbf3c8395",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

pprint(response.json())