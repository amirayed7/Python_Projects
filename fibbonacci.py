import stdio
import sys

# declare n as an integer
n = int(sys.argv[1])

# declare a b and c to numbers given
a = 1
b = 1
i = 3

# create a while loop that exchanges a and b to a plus b
while i <= n:
    temp = a
    a = b
    b = temp + b
    i += 1

# write out b
stdio.writeln(b)
