# write a program for the following requirement
# 'a5z1c2' --> 'aaaaaccz' (alphabetically sorted)


string = input()
output = ''
i = 0

while len(string) > i:
    if string[i].isalpha():
        if (string[i+1]).isdigit():
            output += string[i] * int(string[i+1])
    
        
    i += 1

print(''.join(sorted(output)))