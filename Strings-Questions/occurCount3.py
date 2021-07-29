# write a program for the following pattern
# 'aaabbccc' --> 3a2b3c

string = input()
output = ''
previous = string[0]
count = 0

for i in string:
    if i == previous: count += 1
    else:
        output += (str(count)+previous)
        previous = i
        count = 1

if previous == string[-1]:
    output += (str(count)+previous)

print(output)
