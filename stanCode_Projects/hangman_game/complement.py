"""
File: complement.py
Name: Jason Hsu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program builds the complement of the entered DNA series.
    """
    s1 = input('Please give me a DNA strand and I\'ll find the complement: ')
    s2 = upper(s1)
    dna = build_complement(s2)
    print('The complement of '+s1+' is '+dna)


def upper(string):
    """
    :param string: str, the string to be turned into all upper case
    """
    ans = ''
    for ch in string:
        # turn into all upper series
        if ch.islower():
            ans = ans + ch.upper()
        else:
            ans = ans + ch
    return ans


def build_complement(string):
    """
    :param string: str, the string to be turn into a complement string
    """
    ans = ''
    for i in range(len(string)):
        ch = string[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        else:
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
