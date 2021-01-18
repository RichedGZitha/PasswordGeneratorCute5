#!/bin/python

import string
from random import *

characters = string.ascii_letters+ string.digits +string.ascii_lowercase + string.digits

# get special chars fro system. ROom for Improvement.
specials   = '~`@#$%^&*()_-=+|}]{[:;?/.><",'

def generatePassword(passLength = 20, specialCharNumber = 4):
	
	passwordArray = []

	for u in range(1, passLength):
		charPos = randint(1,len(characters) - 1)
		passwordArray.append(characters[charPos])

	for x in range(1,specialCharNumber + 1):
		specialChar = randint(0, len(specials) - 1 )
		pos = randint(0, passLength - 2)

		passwordArray[pos] = str(specials[specialChar])

	password = "".join(passwordArray)

	return password


