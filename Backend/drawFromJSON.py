import json

# Open the JSON file
with open('C:/Users/seif elaban/Documents/GitHub/NAVERIS/Backend/Pre-Processed Data/Matrix2500Dotsp462102n393989.json') as file:
    data = json.load(file)

# Initialize lists to store the extracted values
lat_list = []
lon_list = []
ws_list = []
wd_list = []
ap_list = []

# Iterate over each object in the JSON data
for obj in data:
    # Extract the values for lat, lon, ws, wd, and ap
    lat = float(obj['lat'])
    lon = float(obj['lon'])
    ws = float(obj['ws'])
    wd = float(obj['wd'])
    ap = float(obj['ap'])

    # Append the values to their respective lists
    lat_list.append(lat)
    lon_list.append(lon)
    ws_list.append(ws)
    wd_list.append(wd)
    ap_list.append(ap)

# Print the lists
# print("Latitude List:", lat_list)
# print("Longitude List:", lon_list)
# print("Wind Speed List:", ws_list)
# print("Wind Direction List:", wd_list)
# print("Air Pressure List:", ap_list)