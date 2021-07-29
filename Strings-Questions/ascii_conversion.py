# write a program for the following requirement
# a4k3b2 --> aeknbd

string = input()
output = ''

for i in string:
    if i.isalpha(): # a | k | b
        x = i
    else:
        output += x + chr(ord(x)+int(i)) # a+4 | k+3 | b+2

print(output)