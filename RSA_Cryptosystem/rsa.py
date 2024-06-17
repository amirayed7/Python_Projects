
import stdio
import stdrandom
import sys
import math


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # set p and q to two random primes from the primes list
    p = _choice(_primes(lo, hi))
    q = _choice(_primes(lo, hi - 1))

    #  set n and m to equations given
    n = p * q
    m = (p - 1) * (q - 1)

    # set key list to a lsit of primes from the range 2,m
    key_list = _primes(2, m)

    # set e_primes to an empty list
    e_primes = []

    # use a for loop to find item in a key list that meets criteria and append to empty list
    for i in key_list:
        if m % i != 0:
            e_primes += [i]

    # get a random prime from the list that meets the criteria
    e = _choice(e_primes)

    # use a while loop to find d that meets the criteria
    d = 1
    while (e * d) % m != 1:
        d += 1

    # return the tuple (n, e, d)
    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return (x ** e) % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return (y ** d) % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # create an empty primes list
    primes_list = []

    # create a nested for loop that finds prime numbers within the range
    for i in range(lo, hi):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break

        # if the number is prime, add to the primes list and return it
        if (is_prime is True) and i > 1:
            primes_list += [i]

    return primes_list


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # create an empty list to store the sample items
    sample_items = []

    # set k to the biggest number that can be sampled from K and the length of list a
    k = min(k, len(a))

    # use a while loo[ to get a random choice from the list a
    while len(sample_items) < k:
        choice = _choice(a)

        # if the choice is not in the list add it and return that list
        if choice not in sample_items:
            sample_items += [choice]

    return sample_items


# Returns a random item from the list a.
def _choice(a):
    return a[stdrandom.uniformInt(0, len(a))]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
