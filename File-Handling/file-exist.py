# Program for check whether a file is exist or not
# it has some bug. future me please fix it

import os

file_name = input('Enter fileName for check ')

if os.path.isfile(file_name):
	print(f'{file_name} is exist')

	print('Reading data from the file =>')
	with open(file_name) as file:
		print(file.read())
else:
	print(f'{file_name} is not exist')

# ==============================================
# Program to print number of lines, characters and words present in the given file

file_name = input('Enter file name ')

if os.path.isfile(file_name):
	print(f'{file_name} is exist')

	line_count = 0
	word_count = 0
	chars_count = 0
	with open(file_name) as file:

		for line in file:
			word_count += len(line.split())
			line_count += 1
			chars_count += len(line)

	print(f'The numbe of line is {line_count}')
	print(f'The number of words are {word_count}')
	print(f'The number of chars are {chars_count}')
	
else:
	print(f'{file_name} is not found')
		
