# write a program to reverse the string without predefined method

string = input()
new_string = ''

for i in range(len(string)):
    new_string += string[len(string)-1-i]

print(new_string)