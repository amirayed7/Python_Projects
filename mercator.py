import math
import stdio
import sys

# Accept lat (float), and lon (float) as command-line arguments.
lat = float(sys.argv[1])
lon = float(sys.argv[2])

# Find x and y values corresponding to the equation given
x = lon
y = (math.log((1 + math.sin(math.radians(lat))) / (1 - math.sin(math.radians(lat))))) / (2)

# Write a message of the values of x and y to standard output.
stdio.writeln(str(x) + " " + str(y))
