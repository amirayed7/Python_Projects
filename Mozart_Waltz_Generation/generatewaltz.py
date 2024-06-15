import stdarray
import stdrandom
import stdio

# read the minuet and trio measures from a 2d list
minuet = stdarray.create2D(11, 16, 0)
trio = stdarray.create2D(6, 16, 0)

# create a for loop that will minuet list
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()

# do the same for the trio list
for i in range(6):
    for j in range(16):
        trio[i][j] = stdio.readInt()

#generate random measures from minuet and print it out
for i in range(16):
    die1 = stdrandom.uniformInt(0, 6)
    die2 = stdrandom.uniformInt(0, 6)
    i = die1 + die2
    j = stdrandom.uniformInt(0, 15)
    minuet2 = f'{minuet[i][j] }'
    stdio.writeln(minuet2)

#Do the same for trio
for i in range(16):
    i = stdrandom.uniformInt(0, 6)
    j = stdrandom.uniformInt(0, 15)
    trio2 = f'{trio[i][j] }'
    stdio.writeln(trio2)

