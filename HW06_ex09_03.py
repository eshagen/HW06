#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

def avoids(word, letters):
	for letter in word:
		# Use letter_check function to determine if a letter occurs in the word
		if (letter_check(letters, letter)):
			return False
		else:
			continue
	else:
		return True

def letter_check(letters, char):
	#Checks each character passed in against the string of forbidden characters.
	for letter in letters:
		if letter == char:
			return True
			break
		else:
			continue

def user_forbidden():
	line_count = 0
	# Allows user to enter the string of forbidden characters.

	forbidden = raw_input("Enter a few letters to 'forbid'\n:")


	with open("words.txt", 'r') as f:
		data = f.readlines()
		# Works through each line of words.txt, passing each line to 'avoids' function.
		for lines in data:
			if (avoids(lines, forbidden)):
				line_count += 1
			else:
				continue
		else:
			return line_count

"""I can't figure part 3 out.  My idea is to count how many times each letter
in the alphabet occurs, and to return the letters which occur most infrequently.
I'm not sure how to do that, will check other's submissions.
"""

##############################################################################
def main():
    print user_forbidden()

if __name__ == '__main__':
    main()
