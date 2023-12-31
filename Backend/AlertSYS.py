import json
from random import randint
import requests
s = []
count = 0
with open("Backend/dotMatrix.json", "r") as db:
    db3 = json.load(db)
    for db2 in db3:
        count += 1 
        if float(db2["ws"]) >= 65 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 65:
            prb = randint(99,80)
            lat = db2["lat"]
            lon = db2["lon"]
            limit = 2
            key = "77df8ee93034bedcbe6b96b0f9eb9f0a"
            res = requests.post(f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={key}')

            s.append({
                "id" : count,
                "wm" : "D",
                "pb" : f"{prb}%",
                "cc" : "null"
            })
        if float(db2["ws"]) >= 50 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 50:
            prb = randint(30,60)
            lat = db2["lat"]
            lon = db2["lon"]
            limit = 2
            key = "77df8ee93034bedcbe6b96b0f9eb9f0a"
            res = requests.post(f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={key}')
            s.append({
                "id" : count,
                "wm" : "W",
                "pb" : f"{prb}%",
                "cc" : "null"
            })
        if float(db2["ws"]) >= 40 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 40:
            prb = randint(0,30)
            lat = db2["lat"]
            lon = db2["lon"]
            limit = 2
            key = "77df8ee93034bedcbe6b96b0f9eb9f0a"
            res = requests.post(f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={key}')
            s.append({
                "id" : count,
                "wm" : "N",
                "pb" : f"{prb}%",
                "cc" : "null"
            })
        file = open('alert.json', 'w')
        json.dump(s,file,indent=4)