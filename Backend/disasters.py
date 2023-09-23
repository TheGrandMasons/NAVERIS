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
        self.red = radius

    def __str__(self):
        return f"Disaster: {self.name}\n Type: {self.type}\nLongitude: {self.longitude}\nLatitude: {self.latitude}\nWindspeed: {self.windspeed}\nWind Direction: {self.wind_direction}\nTectonic Plate: {self.tectonic_plate}\n Heading: {self.heading}\nQuake: {self.magnitude}\nHeading Speed: {self.heading_speed}\nHeading Direction: {self.heading_direction}\nRadius: {self.radius}"

# Example of a disaster.
Taylor = disaster("Taylor", "Earthquake", 26.820553, 30.802498, 0, 0, 0, 0, 0, "Arabian", 6.3)