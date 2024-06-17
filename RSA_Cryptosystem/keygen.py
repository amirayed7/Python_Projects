
import rsa
import stdio
import sys


# Entry point.
def main():
    # set lo and hi as integers
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # call keygen function to get keys as a tuple
    n, e, d = rsa.keygen(lo, hi)

    # write the values of the tuple with a space in between
    stdio.writeln(f"{n} {e} {d}")


if __name__ == '__main__':
    main(
