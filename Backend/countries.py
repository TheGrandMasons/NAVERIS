class country:
    def __init__(self, name, capital, latitude, longitude, windspeed, wind_direction, tectonic_plate):
        self.name = name
        self.cap = capital
        self.lat = latitude
        self.long = longitude
        self.coords = (round(self.lat,2), round(self.long,2))
        self.wind = (windspeed, int(wind_direction))
        self.plate = tectonic_plate

    def __str__(self):
        return f"Country: {self.name}\nCapital: {self.cap}\nLatitude: {self.lat}\nLongitude: {self.long}\nWindspeed: {self.wind[0]}\nWind Direction: {self.wind[1]}\nTectonic Plate: {self.plate}"


# Countries
eg = country("Egypt", "Cairo", 26.820553, 30.802498, 0, 0, "Arabian")
us = country("United States", "Washington", 37.09024, -95.712891, 0, 0, "North American")


# List of countries
countriesList = [
    eg,
    us
    # Add more countries here...
]