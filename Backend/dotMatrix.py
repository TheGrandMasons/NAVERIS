class Dot:
    def __init__(self, id, latitude, longitude, windspeed, wind_direction, pressure):
        self.id = id
        self.lat = latitude
        self.long = longitude
        self.wind = (windspeed, int(wind_direction))
        self.pressure = int(pressure)

    def __str__(self):
        return f"(ID: {self.id}, Latitude: {self.lat}, Longitude: {self.long}, Wind Speed: {self.wind[0]}, Wind Direction: {self.wind[1]}, Pressure: {self.pressure})"

dots = []
startingLatitude = float(input("Enter starting latitude: ")) * 2
startingLongitude = float(input("Enter starting longitude: ")) * 2
windspeed = 10 # Placeholder
wind_direction = 45 # Placeholder
pressure = 1000 # Placeholder

for lat1 in range(int(startingLatitude), int(startingLatitude) + 20):
    for long1 in range(int(startingLongitude), int(startingLongitude) + 20):
        dotID = len(dots) + 1
        new_dot = Dot(dotID, lat1/2, long1/2, windspeed, wind_direction, pressure)
        dots.append(new_dot)

# Now you can access each dot by its index in the list
# for dot in dots:
#     print(dot)