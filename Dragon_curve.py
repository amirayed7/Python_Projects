
import stdio
import sys

# declare n as an integer
n = int(sys.argv[1])

# declare dragon and nogard as a string F
dragon = 'F'
nogard = 'F'

# create a for loop  that exchanges dragon and nogard to exchanges given
for i in range (1, n+1):
    temp = dragon
    dragon = dragon + "L" + nogard
    nogard = temp + "R" + nogard

# write out dragon
stdio.writeln(dragon)
