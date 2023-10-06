from countries import *
from disasters import *
from disasterVector import *
from dotMatrix import *
from plates import *
from plotter import *
import math

#[[Maximum Wind ,  Minimum Pressure ,  Low Wind NE ,   Low Wind SE ,   Low Wind SW ,   Low Wind NW ,   Moderate Wind NE,  Moderate Wind SE,  Moderate Wind SW  , Moderate Wind NW  , High Wind NE    ,  High Wind SE ,      High Wind SW   ,   High Wind NW ]]

max_wind=WS
def resolve_wind_direction(wind_speed, wind_direction):
    # Define the ordinal directions in clockwise order
    directions = ['NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']

    # Calculate the angle between each direction and the input wind direction
    angles = [abs((i * 45) - wind_direction) for i in range(8)]

    # Find the two nearest directions
    nearest_indices = sorted(range(len(angles)), key=lambda i: angles[i])[:2]
    nearest_directions = [directions[i] for i in nearest_indices]

    # Calculate the magnitudes on the nearest directions
    magnitudes = []
    for direction in nearest_directions:
        # Calculate the angle between the nearest direction and the input wind direction
        angle_diff = abs(wind_direction - directions.index(direction) * 45)

        # Calculate the magnitude based on the cosine of the angle difference
        magnitude = wind_speed * math.cos(math.radians(angle_diff))
        magnitudes.append(magnitude)

    return nearest_directions, magnitudes

# Example usage
wind_speed = float(input("Enter the wind speed: "))
wind_direction = float(input("Enter the wind direction (in degrees): "))

nearest_directions, magnitudes = resolve_wind_direction(wind_speed, wind_direction)
print(f"The nearest two ordinal directions are: {nearest_directions[0]} and {nearest_directions[1]}")
print(f"The magnitudes on those directions are: {magnitudes[0]} and {magnitudes[1]}")