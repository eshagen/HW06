#!/usr/bin/env python
# Day 6 ex02
# Read roster.txt and print the number of names containing the letter 'e'
# Function also should print the names

##############################################################################

def print_e():
	e_count = 0
	e_names = []
	# Open file to read
	with open("roster.txt" , "r") as f:
		# Creating 'data' so that I can more easily manipulate contents of roster.txt
		data = f.readlines()
		for line in data:
			for char in line:
				if (char == 'e'):
					#Appending any names with 'e' to a list, incrementing a counter and breaking
					e_names.append(line.strip())
					e_count += 1
					break
		print "There are {0} names containing 'e' in roster.txt.".format(e_count)
		return e_names



##############################################################################
def main():
	print_e()

if __name__ == '__main__':
    main()
