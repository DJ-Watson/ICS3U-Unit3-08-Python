#!/usr/bin/env python3

# Created by DJ Watson
# Created on October 2019
# this program checks if an inputted year is a leap year


def main():
    # input

    numinput = input("Enter year: ")
    # process and output

    try:
        intcheck = int(numinput)
        if int(numinput) >= 0:
            if (int(numinput) % 4 == 0) & (int(numinput) % 100 != 0):
                print("this is a leap year!")
            elif (int(numinput) % 100 == 0) & (int(numinput) % 400 == 0):
                print("this is a leap year!")
            else:
                print("this is not a leap year")
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
