import json
from random import randint
s = []
count = 0
with open("dotmatrix.json", "r") as db:
    fullen = len(db.readlines())
    db3 = json.loads()
    for db2 in db3:
        count += 1 
        if float(db2["ws"]) >= 65 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 65:
            prb = randint(80, 99)
            s.append({
                "id" : count,
                "wm" : "D",
                "pb" : f"{prb}%",
                "cc" : "NULL"
            })
        if float(db2["ws"]) >= 50 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 50:
            prb = randint(60, 30)
            s.append({
                "id" : count,
                "wm" : "W",
                "pb" : f"{prb}%",
                "cc" : "NULL"
            })
        if float(db2["ws"]) >= 40 and int(db2["ap"]) <= 1010 or float(db2["ws"]) >= 40:
            s.append({
                "id" : count,
                "wm" : "N",
                "pb" : f"{prb}%",
                "cc" : "NULL"
            })
