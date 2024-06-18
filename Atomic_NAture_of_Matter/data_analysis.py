
import math
import stdio


def main():
    # Set ETA, RHO, T, and R to values given
    ETA = 9.135e-4
    RHO = 5e-7
    T = 297.0
    R = 8.13457
    METERS_PER_PIXEL = 1.753e-7

    # Set displacements to reading standard input
    displacements = stdio.readAllFloats()

    # Set the squared displacementts added to 0
    squared_displacements_added = 0

    # get the sum of the squares of n displacements
    for n in displacements:
        squared_displacement = (METERS_PER_PIXEL * n) ** 2

        squared_displacements_added += squared_displacement

    # set var to the squared displacements added over 2 times n
    var = squared_displacements_added / (2 * len(displacements))

    # set Boltzmann and Avogardo to equation given
    Boltzmann = 6 * math.pi * var * ETA * RHO / T
    Avogardo = R / Boltzmann

    stdio.writef('%e %e\n', Boltzmann, Avogardo)


if __name__ == '__main__':
    main()
