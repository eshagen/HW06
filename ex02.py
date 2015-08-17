#!/usr/bin/env python
# Day 6 ex02
# Write ten random numbers to a file


##############################################################################
import random

# Body
def write_ten():
	
	for num in range(1,11):
		fin = open("random.txt" , 'a')
		fin.write(str(random.randint(1,25))+"\n")




##############################################################################
def main():
    write_ten()

if __name__ == '__main__':
    main()
