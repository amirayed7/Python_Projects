
import stdio
import sys

# declare n as an integer
n = int(sys.argv[1])

# create four nested while loops that declares the left bound and the right bound is while loop
a = 1
while a * a * a <= n:
    b = a + 1
    while b * b * b <= n - (a * a * a):
        c = a + 1
        while c * c * c <= n:
            d = c + 1
            while d * d * d <= n - (c * c * c):
                # create an if statement that finds the desired total using the equations given
                if ((a * a * a) + (b * b * b)) == ((c * c * c) + (d * d * d)):
                    if (a + b) != (c + d):
                        total = ((a * a * a) + (b * b * b))
                        # write out the total as well as the variables in an f string
                        stdio.writeln(f"{total} = {a}^3 + {b}^3 = {c}^3 + {d}^3")
                d += 1
            c += 1
        b += 1
    a += 1
