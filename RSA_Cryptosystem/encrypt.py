import rsa
import stdio
import sys


# Entry point.
def main():
    # set n and e as integers
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # set width to the bitlength function to get the number of bits per char
    width = rsa.bitLength(n)

    # accept message as an empty string
    message = ""

    # create a while loop so that if stdio is not empty and has a new line then read it and move on
    while not stdio.isEmpty():
        if stdio.hasNextLine():
            message += stdio.readLine()
            message += "\n"

    # for each charecter in message use ord to turn it into an integer abd encrypt it
    for char in message:
        x = ord(char)
        encrypted = rsa.encrypt(x, n, e)

        #Write the encrypted value as a width-long binary string.
        stdio.write(rsa.dec2bin(encrypted, width))
    stdio.writeln("\n")


if __name__ == '__main__':
    main()
