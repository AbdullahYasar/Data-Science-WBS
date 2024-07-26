import requests

url = "https://aerodatabox.p.rapidapi.com/flights/airports/iata/BER/2023-04-04T20:00/2023-04-05T08:00"

querystring = {"withLeg":"true","withCancelled":"true","withCodeshared":"true","withCargo":"true","withPrivate":"true","withLocation":"false"}

headers = {
	"X-RapidAPI-Key": "57e40df905msh89f91a584028707p1724bfjsn063fbf3c8395",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())