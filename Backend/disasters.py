class disaster:
    def __init__(self, name, type, latitude, longitude, windspeed, wind_direction, heading_speed, heading_direction, radius, tectonic_plate, magnitude):
        self.name = name
        self.type = type
        self.lat = latitude
        self.long = longitude
        self.coords = (round(self.lat,2), round(self.long,2))
        self.wind = (windspeed, int(wind_direction))
        self.plate = tectonic_plate
        self.heading = (heading_speed, int(heading_direction))
        self.quake = magnitude
        self.rad = radius

    def __str__(self):
        return f"Disaster: {self.name}\n Type: {self.type}\nLatitude: {self.lat}\nLongitude: {self.long}\nWindspeed: {self.wind[0]}\nWind Direction: {self.wind[1]}\nTectonic Plate: {self.plate}\n Heading: {self.heading}\nQuake: {self.quake}\nHeading Speed: {self.heading[0]}\nHeading Direction: {self.heading[1]}\nRadius: {self.rad}"

# Example of a disaster.
# Taylor = disaster("Taylor", "Earthquake", 26.820553, 30.802498, 0, 0, 0, 0, 0, "Arabian", 6.3)
# print(Taylor.coords)