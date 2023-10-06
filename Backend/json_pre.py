import json
import math

def jsonReady():
    file  = open('Matrix2500Dotsp462102n393989.json', 'r')
    db = json.load(file)
    #print(db)
    #print((db[399])['id'])
    counter = 0
    Wind_matrix = []
    Deg_matrix = []
    Pressure_matrix = []
    maxID = int((db[-1])['id'])
    Range = int(math.sqrt(maxID))
    print(Range)
    for i in range(Range):
        in_speed = []
        in_deg = []
        in_pre = []
        for j in range(Range):

            speed  = float((db[counter])['ws'])
            deg = float((db[counter])['wd'])
            pressure = float((db[counter])['ap'])

            in_speed.append(speed)
            in_deg.append(deg)
            in_pre.append(in_pre)
            counter += counter
            j =j+1

        Wind_matrix.append(in_speed)
        Deg_matrix.append(in_deg)
        Pressure_matrix.append(in_pre)
        i = i + 1
    return Wind_matrix , Deg_matrix , Pressure_matrix
jsonReady()