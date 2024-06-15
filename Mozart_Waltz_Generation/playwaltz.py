import stdaudio
import stdio
import sys
import playsound

#read the waltz measures from standard input into a 1d list
waltz_measures = stdio.readAllInts()

# if the measure is not equal to 32 then print the error message
if len(waltz_measures) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

# if the minuet measure is not in the range then print the error message
for i in range(16):
    if waltz_measures[i] < 1 or waltz_measures[i] > 176:
        sys.exit("A minuet measure must be from [1, 176]")

# if the trio measure is not in the range then print the error message
for i in range(16, 32):
    if waltz_measures[i] < 1 or waltz_measures[i] > 96:
        sys.exit("A trio measure must be from [1, 96]")

#Play the first 16 minuet measures
for i in range(16):
    playsound.playsound(f"data/M{waltz_measures[i]}.wav")

#Play the last 16 trio measures
for i in range(17,32):
    playsound.playsound(f"data/T{waltz_measures[i]}.wav")
