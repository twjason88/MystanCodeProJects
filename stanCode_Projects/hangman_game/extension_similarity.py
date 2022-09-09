"""
File: similarity.py (extension)
Name: Jason Hsu
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program finds the best similarity segment of the two entered DNA sequences
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')
    ans = match(long_sequence, short_sequence)
    print('The best match is '+ans)


def match(a, b):
    """
    :param a: str, the long_sequence DNA to be mated
    :param b: str, the short_sequence DNA to be mated
    :return: str, the best matched DNA series
    """
    a = upper(a)
    # make string, a, case-insensitive
    b = upper(b)
    # make string, b, case-insensitive
    maximum = 0
    # set the smallest value of maximum
    the_one = ''
    find_f = len(a)-len(b)+1
    # the number of frequency that short_sequence have to match
    for i in range(find_f):
        n = 0
        # the number of matched DNA character
        seq = a[i:len(b)+i]
        # the small sequence of the long_sequence DNA during each match
        for j in range(len(seq)):
            ch_a = seq[j]
            if ch_a == b[j]:
                n += 1
        semblance = n / len(b)
        # the similarity of the two entered DNA (shor_sequence and divided long_sequence)
        if semblance > maximum:
            # find maximum
            maximum = semblance
            the_one = seq
            # store the best match segment
    return the_one


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


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
