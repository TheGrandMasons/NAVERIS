import numpy as np
import matplotlib.pyplot as plt
from dotMatrix import *
from json_pre import *

def draw(lat, long, range, resolution):
    makeDots(lat, long, range, resolution)
    # Your wind direction data in degrees, basically put the output deg_matrix in here.
    direction_degrees = np.array(deg_matrix)
    # Convert to radians
    direction_matrix = np.radians(direction_degrees)

    # Assuming a constant wind speed of 1 for all directions and here put the output speed_matrix.
    speed_matrix_draw = np.array(speed_matrix)

    X, Y = np.meshgrid(np.arange(direction_matrix.shape[1]), np.arange(direction_matrix.shape[0]))

    U = speed_matrix_draw * np.cos(direction_matrix)
    V = speed_matrix_draw * np.sin(direction_matrix)

    plt.figure()
    plt.quiver(X, Y, U, -V, speed_matrix_draw, cmap='jet', scale=500) # type: ignore
    plt.colorbar(label='Wind Speed')
    plt.title('Wind Speed and Direction')
    plt.show()

def drawJSON():
    Wind_Speed, Wind_Deg, Pressure = jsonReady()
    # Your wind direction data in degrees, basically put the output deg_matrix in here.
    direction_degrees = np.array(Wind_Deg)
    # Convert to radians
    direction_matrix = np.radians(direction_degrees)

    # Assuming a constant wind speed of 1 for all directions and here put the output speed_matrix.
    speed_matrix_draw = np.array(Wind_Speed)

    X, Y = np.meshgrid(np.arange(direction_matrix.shape[1]), np.arange(direction_matrix.shape[0]))

    U = speed_matrix_draw * np.cos(direction_matrix)
    V = speed_matrix_draw * np.sin(direction_matrix)

    plt.figure()
    plt.quiver(X, Y, U, -V, speed_matrix_draw, cmap='jet', scale=500) # type: ignore
    plt.colorbar(label='Wind Speed')
    plt.title('Wind Speed and Direction')
    plt.show()