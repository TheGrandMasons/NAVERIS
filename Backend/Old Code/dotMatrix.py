import requests
import json
import time

class Dot:
    def __init__(self, id, latitude, longitude, windspeed, wind_direction, pressure, time):
        self.id = id
        self.lat = latitude
        self.long = longitude
        self.wind = (windspeed, int(wind_direction))
        self.pressure = int(pressure)
        self.matrix = (windspeed, int(wind_direction), int(pressure))
        self.data = (id, latitude, longitude, windspeed, int(wind_direction), int(pressure))
        self.time = time

    def __str__(self):
        return f"(ID: {self.id}, Latitude: {self.lat}, Longitude: {self.long}, Wind Speed: {self.wind[0]}, Wind Direction: {self.wind[1]}, Pressure: {self.pressure}, Time: {self.time})"

dots = []
startingLatitude = float(input("Enter starting latitude: ")) * 2
startingLongitude = float(input("Enter starting longitude: ")) * 2

for lat1 in range(int(startingLatitude), int(startingLatitude) + 5): 
    for long1 in range(int(startingLongitude), int(startingLongitude) + 5):
        dotID = len(dots) + 1
        # Requests Constants.
        lon = long1/2
        lat = lat1/2
        def Status(lon, lat):
            # Requests Constants.
            API_Key = "77df8ee93034bedcbe6b96b0f9eb9f0a"
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"
            # Sending Req.
            response = requests.get(url)
            # Get The Response With Json Format.
            res = response.json()

            if res["cod"] != "404":
                #data = res['main']
                live_wind_speed = res["wind"]["speed"]
                live_pressure = res["main"]["pressure"]
                live_wind_degree = res["wind"]["deg"]
                current_time = time.strftime("%H:%M:%S", time.localtime()) 
                new_dot = Dot(dotID, lat1/2, long1/2, live_wind_speed, live_wind_degree, live_pressure, current_time)
                dots.append(new_dot)
            else:
                return "Error While Fetching The Response Of API Request."
        Status(lat,lon)

# Print the dot matrix.
# for dot in dots:
#     print(dot.data)