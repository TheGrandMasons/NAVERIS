import json
def detect(raw_database):
    database = open(raw_database)
    file = json.load(database)
    for single_raw in file:
        ws = single_raw["ws"]
        ap = single_raw["ap"]
        if ws > 49:
            
detect("dotMatrix.json")