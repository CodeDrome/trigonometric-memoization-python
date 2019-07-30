import math

import trigonometricmemoization


def main():

    print("-----------------------------")
    print("| codedrome.com             |")
    print("| Trigonometric Memoization |")
    print("-----------------------------\n")

    degrees_in_radian = 180.0 / math.pi

    tm = trigonometricmemoization.TrigonometricMemoization()

    print("-" * 70)
    print("| Degrees |       Sines       |      Cosines     |      Tangents     |")
    print("-" * 70)

    for d in range(-720, 721, 15):

        print("| {:7d} ".format(d), end="")

        print("| {:7.4f} | {:7.4f}".format(math.sin(d / degrees_in_radian), tm.sine(d)), end="")

        print(" | {:7.4f} | {:7.4f}".format(math.cos(d / degrees_in_radian), tm.cosine(d)), end="")

        if( ((d - 90) % 180) != 0):
            print("| {:7.4f} | {:7.4f} |".format(math.tan(d / degrees_in_radian), tm.tangent(d)))
        else:
            print("|       ~ | {:7.4f} |".format(tm.tangent(d)))

    print("-" * 70)


main()
