"""
File: name_sq.py (extension)
Name: Jason Hsu
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    This program turns the inputted name into a square pattern!
    """
    print('This program prints a name in a square pattern!')
    name = input('Name: ')
    square(name)


def square(string):
    """
    :param string: str, the entered string to be turned into a square pattern
    """
    print(string)
    # the first part of the square pattern, normal name
    for i in range(len(string)-2):
        # the middle part of the square
        result = ''
        for j in range(len(string)):
            if j == 0:
                result += string[1+i]
                # the first character of each line in the middle part
            elif j == len(string)-1:
                result += string[len(string)-2-i]
                # the last character of each line in the middle part
            else:
                # the remain characters of each line in the middle part
                result = result + ' '
        print(result)
    reverse(string)


def reverse(string):
    """
    :param string: str, the string to be reversed
    """
    result_last = ''
    for ch in string:
        # print the last line in the square pattern, reversing the name
        result_last = ch + result_last
    print(result_last)


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
