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
        self.dataForJSON = f'[\n\t"id": "{id}",\n\t"lat": "{latitude}",\n\t"lon": "{longitude}",\n\t"ws": "{round(windspeed,2)}",\n\t"wd": "{int(wind_direction)}",\n\t"ap": "{int(pressure)}",\n\t"tm": "{time}"\n]'
        self.time = time
        self.dataModel = f'{windspeed},{wind_direction},{pressure},'

    def __str__(self):
        return f"[ID: {self.id}, Latitude: {self.lat}, Longitude: {self.long}, Wind Speed: {self.wind[0]}, Wind Direction: {self.wind[1]}, Pressure: {self.pressure}, Time: {self.time}]"

def Status(lat, lon):
    API_Key = "77df8ee93034bedcbe6b96b0f9eb9f0a"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"

    response = requests.get(url)
    res = response.json()
    # print(res)
    if res["cod"] != "404":
        # Extract data from res (output data from the api).
        speed = res['wind']['speed'] * 3.6
        deg = res['wind']['deg']
        pres = res['main']['pressure']
        return speed, deg, pres
    else:
        return "Error While Fetching The Response Of API Request."

deg_matrix = []
speed_matrix = []
pres_matrix = []
dots = []
def makeDots(latf, lonf, range, resolution):
    f = open("dotMatrix.json", "w")
    f.write("[\n")
    global deg_matrix
    global speed_matrix
    global pres_matrix
    global dots
    startingLatitude = float(latf) # float(input("Enter starting latitude: "))
    startingLongitude = float(lonf) # float(input("Enter starting longitude: "))

    nlat = startingLatitude
    stopping_lat = startingLatitude - range
    stopping_lon = startingLongitude + range
    loop = 1
    while startingLatitude > stopping_lat:
        
        # nlon is a placeholder for the starting lon.
        nlon = startingLongitude
        deg_matrix_in = []
        speed_matrix_in = []
        pres_matrix_in = []
        while nlon < stopping_lon:
            # Get the current speed, degree and pressure.
            speed, deg, pres = Status(startingLatitude,nlon)
            nlon = nlon + resolution
            # Objectify the dot.
            dotID = len(dots) + 1
            current_time = time.strftime("%H:%M:%S", time.localtime())
            new_dot = Dot(dotID, startingLatitude, nlon, speed, deg, pres, current_time)
            dots.append(new_dot)         
            # Append the data to the inner matrix.
            deg_matrix_in.append(deg)
            speed_matrix_in.append(speed)
            pres_matrix_in.append(pres)

            dotData = str(new_dot.dataForJSON)
            dotData = dotData.replace("[", "{")
            dotData = dotData.replace("]", "}")
            f.write('\t' + dotData)
            if new_dot.id < ((range / resolution) ** 2):
                f.write(",\n")
            else:
                f.write("\n") 
        # Append the appeneded data to the main matrix.
        deg_matrix.append(deg_matrix_in)
        speed_matrix.append(speed_matrix_in)
        pres_matrix.append(pres_matrix_in)

        startingLatitude = startingLatitude - resolution
        print('Gathating Data', loop, 'of', int(range/resolution))
        loop = loop + 1
    print("Gathered Data Done.")
    f.write("]")
    return deg_matrix, speed_matrix, pres_matrix

# print('____DEGREE_____')
# print(deg_matrix)
# print('____SPEED_____')
# print(speed_matrix)
makeDots(10, 10, 10,0.5)