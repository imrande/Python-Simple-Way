# write a program for remove duplicate characters from given string

string = input()
output = ''

for ch in string:
    if ch not in output: output += ch

print(output)

# 2nd way
string2 = input()
output = ''.join(set(string2))
print(output)