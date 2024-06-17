import rsa
import stdio
import sys


# Entry point.
def main():
    # accept n and d as integers
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # set width to the bitlength function to get the number of bits per char
    width = rsa.bitLength(n)

    # accept message from standard input
    message = stdio.readString()

    # create a for loop for the length of message within the range and increments by width
    for i in range(0, len(message)-1, width):

        # set s to the substring of message and y as the decimal representation
        s = message[i:i+width]
        y = int(s, 2)

        # decrypt y and accept it as decrypted
        decrypted = rsa.decrypt(y, n, d)

        # write out the  character corresponding to the decrypted value
        stdio.write(chr(decrypted))

if __name__ == '__main__':
    main()
