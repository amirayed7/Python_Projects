
import stdio
import sys

#declare p and q as integers
p = int(sys.argv[1])
q = int(sys.argv[2])

# create a while loop that swap p and q as long as there remainder is not 0
while p % q != 0:
    temp = p
    p = q
    q = temp % q

# write out q
stdio.writeln(q)
