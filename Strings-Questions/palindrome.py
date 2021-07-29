# string is said to be palindrome if it's original str and reversed str are same

string = input()

def palindrome_check(string):
    return string == string[::-1]

print(palindrome_check(string))