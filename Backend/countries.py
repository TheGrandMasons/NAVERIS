class country:
    def __init__(self, name, capital, latitude, longitude, windspeed, wind_direction, tectonic_plate):
        self.name = name
        self.cap = capital
        self.lat = latitude
        self.long = longitude
        self.cord = (round(self.lat,2), round(self.long,2))
        self.wind = (windspeed, int(wind_direction))
        self.plate = tectonic_plate

    def __str__(self):
        return f"Country: {self.name}\nLongitude: {self.longitude}\nLatitude: {self.latitude}\nWindspeed: {self.windspeed}\nWind Direction: {self.wind_direction}\nTectonic Plate: {self.tectonic_plate}"
    
# Countries
eg = country("Egypt", "Cairo", 26.820553, 30.802498, 0, 0, "Arabian")
    # reate a list of countries
countriesList = {
    eg
    # Add more countries here...
}