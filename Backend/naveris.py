from countries import *
from disasters import *
from disasterVector import *
from dotMatrix import *
from plates import *
from plotter import *

# To draw a dot matrix use the function draw, in this fomrat:
# draw(lat, long, range, resolution)
# Lat & Long are for geopositioning.
# Range is how many (Lat or Long) lines will be passed.
# Resolution is the distance between each dot measured in (Lat or Long).
# makeDots(10, 10, 2, 0.2)