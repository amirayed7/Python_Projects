
import stdio
import stdrandom
import random

# declare rank as a random integer between 2 and 14
rank = random.randrange(2, 15)

# create an if statement to a string equal to the integer from rank
if rank == 2:
    rankStr = "2"
elif rank == 3:
    rankStr = "3"
elif rank == 4:
    rankStr = "4"
elif rank == 5:
    rankStr = "5"
elif rank == 6:
    rankStr = "6"
elif rank == 7:
    rankStr = "7"
elif rank == 8:
    rankStr = "8"
elif rank == 9:
    rankStr = "9"
elif rank == 10:
    rankStr = "10"
elif rank == 11:
    rankStr = "Jack"
elif rank == 12:
    rankStr = "Queen"
elif rank == 13:
    rankStr = "King"
elif rank == 14:
    rankStr = "Ace"

# declare suit as a random integer between 1 and 4
suit = random.randrange(1, 5)

# create an if statement that represents the suits as strings
if suit == 1:
    suitStr = "Clubs"
elif suit == 2:
    suitStr = "Diamonds"
elif suit == 3:
    suitStr = "Hearts"
elif suit == 4:
    suitStr = "Spades"

# print out the ranks and suits as a string
stdio.writeln(f"{rankStr} of {suitStr}")
