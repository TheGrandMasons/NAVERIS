class country:
    def __init__(self, name, capital, longitude, latitude, windspeed, wind_direction, tectonic_plate):
        self.name = name
        self.cap = capital
        self.long = longitude
        self.lat = latitude
        self.wind = (windspeed, int(wind_direction))
        self.plate = tectonic_plate

    def __str__(self):
        return f"Country: {self.name}\nLongitude: {self.longitude}\nLatitude: {self.latitude}\nWindspeed: {self.windspeed}\nWind Direction: {self.wind_direction}\nTectonic Plate: {self.tectonic_plate}"