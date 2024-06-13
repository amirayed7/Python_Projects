import stdio
import sys

# Accept n1 (int), n2 (int), and p (float) as command-line arguments.
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# Let q be the probability that player two wins
q = 1 - p

# Assuming an unfair coin, let p1 and p2 be the probability that either or end penniless
p1 = (((1) - ((p/q)**n2)) / ((1) - ((p/q)**(n1 + n2))))

p2 = (((1) - ((q/p)**n1)) / ((1) - ((q/p)**(n1 + n2))))

# Write a message of the values of p1 and p2 to standard output.
stdio.writeln(str(p1) + ' ' + str(p2))
