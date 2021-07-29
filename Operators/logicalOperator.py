# logical operators `and or not`
# and -> If both arguments are True then only result is True
# or -> If at least one argument is True then result is True

userName = input('Enter username: ').lower()
password = input('Enter password: ').lower()

print('valid user') if userName == 'durga' and password == 'sunny' else print('Invalid user')