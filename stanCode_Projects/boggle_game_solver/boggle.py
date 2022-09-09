"""
File: boggle.py
Name: Jason Hsu
----------------------------------------
This program finds the words from the input letters in a 4x4 square with a "boggle" way.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Constants
ROW = 4
COLUMN = 4


def main():
	"""
	This program finds the words from the input letters in a 4x4 square with a "boggle" way.
	"""
	####################
	letter_dict = input_letter(ROW, COLUMN)
	if letter_dict is not None:  # Determine whether there is any illegal input letter
		start = time.time()
		dict_dict = read_dictionary(FILE)
		word_num = find_word(letter_dict, dict_dict)
		print(f'There are {word_num} words in total.')
		####################
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_letter(row: int, column: int) -> dict:
	"""
	This function lets users input letters into a 4x4 square and checks whether in a determined manner.
	:param row: int, the row of input letters
	:param column: int, the column of input letters
	:return letter_dict: dict, letters with coordination
	"""
	switch = False  # Set a switch to decide when to stop users from inputting letters
	letter_dict = {}
	for i in range(row):
		if not switch:
			letters = input(f'{i+1} row of letters: ')
			for j in range(len(letters)):  # Check each row of the input letters
				if j % 2 == 0:
					if len(letters[j]) != 1:
						switch = True
						break
					else:
						letter_dict[(j//2, i)] = letters[j].lower()  # Set a coordination for each legal input letter
				else:
					if letters[j] != ' ':
						switch = True
						break
		else:
			print('Illegal input')
			break
	if len(letter_dict) == row*column:
		return letter_dict


def find_word(letter_dict: dict, dict_dict: dict) -> int:
	"""
	This function finds words that match the words in the dictionary from input letters.
	:param letter_dict: dict, input letters with coordination
	:param dict_dict: dict, words in the dictionary
	:return count[0]: int, the number of words found
	"""
	letter_check = []  # Create a list to stop adding letters that have been added in the current string
	count = [0]  # Count the total number of words found
	for key in letter_dict:
		letter_check.append(key)
		find_word_helper(letter_dict, dict_dict, ''+letter_dict[key], letter_check, count)
		letter_check.clear()
	return count[0]


def find_word_helper(letter_dict: dict, dict_dict: dict, current_str: str, letter_check: list, count: list):
	"""
	This helper function finds words that match the words in the dictionary from input letters.
	:param letter_dict: dict, input letters with coordination
	:param dict_dict: dict, words in the dictionary
	:param current_str: str, a string constructed to match words in the dictionary
	:param letter_check: list, store coordination of each letter to prevent adding letters repeatedly
	:param count: int, the number of words found
	"""
	if len(current_str) > ROW*COLUMN:  # Base Case
		pass
	if len(current_str) >= 4 and current_str in dict_dict:  # Base Case
		print(f'Found \"{current_str}\"')
		count[0] += 1
		del dict_dict[current_str]  # Delete a found word in the dictionary to keep searching words with a longer length
		find_word_helper(letter_dict, dict_dict, current_str, letter_check, count)
	else:
		# Find neighbors of the last letter added
		for x in range(letter_check[-1][0]-1, letter_check[-1][0]+2):
			for y in range(letter_check[-1][1]-1, letter_check[-1][1]+2):
				if 0 <= x <= COLUMN-1 and 0 <= y <= ROW-1:  # Prevent finding neighbors out off the 4x4 square
					if (x, y) not in letter_check:
						# Choose
						current_str += letter_dict[(x, y)]
						letter_check.append((x, y))
						# Explore
						if has_prefix(current_str, dict_dict):
							find_word_helper(letter_dict, dict_dict, current_str, letter_check, count)
						# Unchoose
						current_str = current_str[:-1]
						letter_check.pop()


def read_dictionary(file: str) -> dict:
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python dictionary
	:param file: str, the filepath of a dictionary
	:return dict_dict: dict, all the words in the dictionary
	"""
	dict_dict = {}
	with open(file, 'r') as f:
		for line in f:
			line = line.strip()
			dict_dict[line] = 0
	return dict_dict


def has_prefix(sub_s: str, dict_dict: dict) -> bool:
	"""
	This function check whether the word in the dictionary starts with a sub_s.
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_dict: dict, all the words in the dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_dict:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
