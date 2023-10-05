import json
from random import randint
s = []
count = 0
with open("dotMatrix.json", "r") as db:
    db3 = json.load(db)
    for db2 in db3:
        count += 1 
        if float(db2["ws"]) >= 65 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 65:
            prb = randint(99,80)
            s.append({
                "id" : count,
                "wm" : "D",
                "pb" : f"{prb}%",
                "cc" : "NULL"
            })
        if float(db2["ws"]) >= 50 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 50:
            prb = randint(30,60)
            s.append({
                "id" : count,
                "wm" : "W",
                "pb" : f"{prb}%",
                "cc" : "NULL"
            })
        if float(db2["ws"]) >= 40 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 40:
            prb = randint(0,30)
            s.append({
                "id" : count,
                "wm" : "N",
                "pb" : f"{prb}%",
                "cc" : "NULL"
            })
        file = open('alert.json', 'w')
        json.dump(s,file,indent=4)