# There is 5 methods for changing case in string
# upper(), lower(), swapcase(), title(), capitalize()

# program to check 2 strings are equal or not by ignoring case

str1 = input().lower()
str2 = input().lower()

print('Both are equal') if str1 == str2 else print('not equal')

# write an application to check provided username and password are valid or not and 
# username is not case sensitive and password should be case sensitive

username = input('Username: ').lower()
password = input('Password: ')

print('Matched') if username == 'durga' and password == 'Anushka' else print('Not matched')

# write an application where first and last char is upper case and remaining all characters are lower case
string = input()

print(f'{string[0].upper()}{string[1:-1]}{string[-1].upper()}')