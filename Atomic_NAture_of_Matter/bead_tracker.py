
import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # set pixels, tau, delta to what was given
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    # set frames to sys.argv4 and onward
    frames = sys.argv[4:]

    #set prevBeads as a list of beads from frames
    prevBeads = BlobFinder(Picture(frames[0]), tau).getBeads(pixels)

    # For each bead currBead in currBeads, find a bead prevBead from prevBeads that is no further than delta and is
    # closest to currBead, and if such a bead is found, write its distance (using format string ’%.4f\n’) to currBead.

    for i in range(1, len(frames)):
        bf = BlobFinder(Picture(frames[i]), tau)
        currBeads = bf.getBeads(pixels)

        for currBead in currBeads:
            x = math.inf
            for prevBead in prevBeads:
                if currBead.distanceTo(prevBead) <= delta and currBead.distanceTo(prevBead) < x:
                    x = currBead.distanceTo(prevBead)
            if x != math.inf:
                stdio.writef("%.4f\n", x)

        #write a newline charecter
        stdio.writeln()

        #set prevBeads to currBeads
        prevBeads = currBeads


if __name__ == '__main__':
    main()
