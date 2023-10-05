import json
def detect(database):
    database2 = open(database)
    file = json.load(database2)
    print(file[1])
detect("dotMatrix.json")