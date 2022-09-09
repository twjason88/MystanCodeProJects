"""
File: caesar.py
Name: Jason Hsu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program deciphers the string entered!
    """
    i = int(input('Secret number: '))
    s = input('What\'s the ciphered string? ')
    s1 = upper(s)
    new_alphabet = move(ALPHABET, i)
    new_word = find(new_alphabet, ALPHABET, s1)
    print('The deciphered string is: '+new_word)


def upper(string):
    """
    :param string: str, the string to be turned into all upper case
    :return: str, the string in all upper case
    """
    ans = ''
    for ch in string:
        # turn into all upper series
        if ch.islower():
            ans = ans + ch.upper()
        else:
            ans = ans + ch
    return ans


def move(string, i):
    """
    :param string: str, the order of a string to be moved based on the number i
    :param i: int, the number to move the order of a string
    :return: str, the moved string
    """
    ans = string[25-i+1:]
    # the letters to be moved from rear to front
    ans += string[:25-i+1]
    # the remained letters
    return ans


def find(new_alphabet, alphabet, s1):
    """
    :param new_alphabet: str, the string to be based on to find the order of the letters in s1
    :param alphabet: str, the string based on the correct order to be used to find readable string
    :param s1: the entered string
    :return: str, the readable string
    """
    ans = ''
    for ch in s1:
        i = new_alphabet.find(ch)
        if i == -1:
            # the entered string of a sentence considering ' ' and '!'
            ans += ch
        ans += alphabet[i:i+1]
        # build up each correct letter
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
