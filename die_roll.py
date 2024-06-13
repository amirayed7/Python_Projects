import stdio
import stdrandom
import sys

# Accept n (int) as a command line arguement
n = int(sys.argv[1])

# Set n to a random integer between 1 and (n+1), obtained by calling stdrandom.uniformInt().
n = stdrandom.uniformInt(1,(n+1))

# Write the sum of two rolls to standard output
stdio.writeln(n + n)
