import requests
import datetime as dt

# Global Variables for latitude and longitude
lan_lat = 42.688050
lan_long = -84.562998

parameters = {
    "lat": lan_lat,
    "lng": lan_long,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

current_time = dt.datetime.now()
# Printing only the current daytime hour
print(current_time.hour)
# Printing only the sunrise/sunset hour
print(sunrise)
print(sunset)

