# Program to generate 6 random numbers which can be used as OTP

import random
from string import ascii_letters

random_password = ''
for i in range(1, 7):
	random_password += str(random.randint(0, 9))

print(random_password)


# Generate a random password of 6 length where 1, 3, 5 are numbers and 2, 4, 6 are alphabets...

random_password = ''
for i in range(1, 7):
	if i % 2 == 0:
		random_password += random.choice(ascii_letters)
	else:
		random_password += str(random.randint(0, 9))

print(random_password)

