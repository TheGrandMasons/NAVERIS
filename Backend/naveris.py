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
# draw(46.2102, -39.3989, 10, 0.5)
# drawJSON()