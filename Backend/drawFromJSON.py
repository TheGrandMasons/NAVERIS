import json
import numpy as np
import matplotlib.pyplot as plt
# Open the JSON file
with open('dotMatrix.json') as file:
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
def drawJSON():
    direction_degrees = np.array(wd_list)
    # Convert to radians
    direction_matrix = np.radians(direction_degrees)

    # Assuming a constant wind speed of 1 for all directions and here put the output speed_matrix.
    speed_matrix_draw = np.array(ws_list)

    X, Y = np.meshgrid(np.arange(direction_matrix.shape[1]), np.arange(direction_matrix.shape[0]))

    U = speed_matrix_draw * np.cos(direction_matrix)
    V = speed_matrix_draw * np.sin(direction_matrix)

    plt.figure()
    plt.quiver(X, Y, U, -V, speed_matrix_draw, cmap='jet', scale=2000) # type: ignore
    plt.colorbar(label='Wind Speed')
    plt.title('Wind Speed and Direction')
    plt.show()
drawJSON()