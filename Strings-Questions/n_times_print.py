# write a program for the following requirement
# 'a5b7c2' --> 'aaaaabbbbbbbcc'

string = input()
output = ''
i = 0

while len(string) > i:
    if string[i].isalpha():
        if (string[i+1]).isdigit():
            output += string[i] * int(string[i+1])
    i += 1

print(output)