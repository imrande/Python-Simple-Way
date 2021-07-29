# Program to specify file name and data dynamically from keyboard

import re

file_name = input('Enter the file: ')
pattern = r'[a-z0-9A-Z]+[\.][txt]+'
match = re.fullmatch(pattern, file_name)
file = open(file_name, 'w')

if match is None:
    print('only .txt file is allowed')
else:
    while True:
        data = input('Write data: ')
        file.write(data + '\n')

        option = input('DO you wanna write more data[y\n] ')
        if option.lower() == 'n': break

file.close()
