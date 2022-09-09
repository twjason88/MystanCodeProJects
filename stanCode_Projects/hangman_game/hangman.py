"""
File: hangman.py
Name: Jason Hsu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays the HANGMAN GAME to guess the correct word!!
    """
    word = random_word()
    dash_word = dash(word)
    guess(dash_word, word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def dash(string):
    """
    :param string: str, the string to be turned into '-' series
    :return: str, the string with only '-' factors
    """
    ans = ''
    for i in range(len(string)):
        ans += '-'
    return ans


def guess(dash_word, word):
    """
    :param dash_word: str, the string to be used to present as the first hidden string where no character entered
    :param word: str, the answer string used to check the correctness
    """
    n = 7
    # total lives
    ans = dash_word
    # the first hidden string
    print('The word looks like '+ans)
    print('You have '+str(n)+' wrong guesses left.')
    while True:
        # stay in while loop until ans == word
        input_ch = input('Your guess: ')
        input_ch = upper(input_ch)
        # make input_ch case-insensitive
        if input_ch.isalpha():
            # check useful inputs
            if input_ch in word:
                print('You are correct!')
                ans = find_word(ans, input_ch, word)
                # reassign ans with function, find_word()
                if ans == word:
                    # check whether it can get out of the while loop
                    print('You win!!')
                    break
                else:
                    print('The word looks like ' + ans)
                    print('You have ' + str(n) + ' wrong guesses left.')
            else:
                n -= 1
                # guessing wrong loses one life
                print('There is no '+input_ch+'\'s in the word.')
                if n != 0:
                    # check whether it can get out of the while loop
                    print('The word looks like '+ans)
                    print('You have '+str(n)+' wrong guesses left.')
                else:
                    print('You are completely hung : (')
                    break
        else:
            # unavailable inputs
            print('Illegal format.')
    print('The word is: '+word)


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


def find_word(ans, input_ch, word):
    """
    :param ans: str, the string to be manipulated
    :param input_ch: str, the inputted character
    :param word: str, the answer string
    :return: str, reassign ans to become more close to the answer
    """
    ans1 = ''
    # string manipulation, start with an empty string
    for i in range(len(word)):
        ch = word[i]
        # look over the old string
        if input_ch == ch:
            # put the correct inputted character in
            ans1 += ch
        else:
            # remain other characters hidden
            ans1 += ans[i:i+1]
    return ans1


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
