
import stdio
import sys

# declare t and v as floats
t = float(sys.argv[1])
v = float(sys.argv[2])

# declare w as the equation provided
w = (35.74 + (0.6215 * t)) + (((0.4275 * t) - 35.75) * (v ** 0.16))

# created an if statement that writes the wind chill w if values of t and v are met
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")
elif v <= 3:
    stdio.writeln("Value of v must be > 3 mph")
else:
    stdio.writeln(w)
