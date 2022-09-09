"""
File: rocket.py
Name: Jason Hsu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program builds a Taiwanese brand-new rocket!!
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE - i):
            # print spaces
            print(' ', end='')
        for j in range(i + 1):
            # print /s
            print('/', end='')
        for j in range(i + 1):
            # print \s
            print('\\', end='')
        for j in range(SIZE - i):
            # print spaces again
            print(' ', end='')
        print('')


def belt():
    for i in range(1):
        for j in range(1):
            # print +
            print('+', end='')
        for j in range(2 * SIZE):
            # print =
            print('=', end='')
        for j in range(1):
            # print + again
            print('+', end='')
        print('')


def upper():
    for i in range(SIZE):
        for j in range(1):
            # print |
            print('|', end='')
        for j in range(SIZE - 1 - i):
            # print .s
            print('.', end='')
        for j in range(i + 1):
            # print /\s, consider these two factors together
            print('/\\', end='')
        for j in range(SIZE - 1 - i):
            # print .s again
            print('.', end='')
        for j in range(1):
            # print | again
            print('|', end='')
        print('')


def lower():
    for i in range(SIZE):
        for j in range(1):
            # print |
            print('|', end='')
        for j in range(i):
            # print .s
            print('.', end='')
        for j in range(SIZE - i):
            # print /\s, consider these two factors together
            print('\\/', end='')
        for j in range(i):
            # print .s again
            print('.', end='')
        for j in range(1):
            # print | again
            print('|', end='')
        print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
    main()
