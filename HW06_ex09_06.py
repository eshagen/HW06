#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports
import string


def is_abecedarian(s):
	if len(s) <= 1:
		return True
	if s[0] > s[1]:
		return False
	return is_abecedarian(s[1:])

""" I definitely got online help for this one.  The 'return is_abecedarian(s[1:])'
line never would've occurred to me, but seems so obvious after seeing it.
"""

def total_abecedarian():
	# Pretty basic, just set up a counter to count the number of lines in words.txt
	# that are abecedarian.
	abc_counter = 0

	with open("words.txt", 'r') as f:
		data = f.readlines()
		for lines in data:
			if is_abecedarian(lines.strip()):
				abc_counter += 1
		return abc_counter

##############################################################################
def main():
    print total_abecedarian()

if __name__ == '__main__':
    main()
