#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

def has_no_e():
	# Keep count of the total words containing e or no e for later % calculation.
	e_count = 0.0
	no_e_count = 0.0

	with open ("words.txt", "r") as f:
		data = f.readlines()
		for lines in data:
			if has_e(lines):
				e_count +=1
			else:
				no_e_count +=1
				# Calculated the % of words without 'e'
				percent = ((no_e_count/(e_count + no_e_count))*100)
				print lines.strip() + " Percentage without 'e' {0}%".format(str(percent))


def has_e(s):
	# This function looks at each character in a string to see if 'e' ever appears.
	for char in s:
		if char == 'e':
			return True
			break
		else:
			continue


##############################################################################
def main():
    has_no_e()

if __name__ == '__main__':
    main()
