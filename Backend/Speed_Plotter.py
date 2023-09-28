import numpy as np
import matplotlib.pyplot as plt
from dotMatrix import *

wind_speeds = np.array()  # replace with your actual data

# Create a contour plot
plt.figure(figsize=(10, 8))
plt.contourf(wind_speeds, cmap='viridis', levels=20)  # Adjust the 'levels' parameter for more or less contours

plt.gca().invert_yaxis()

plt.colorbar(label='Wind Speed (m/s)')

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Wind Speeds')

plt.show()
