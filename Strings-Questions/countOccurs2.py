# write a program for the following pattern
# 'abaabbca' -> 4a3b1c

string = input()
dictionary = {}
output = ''

for ch in sorted(string):
    dictionary[ch] = dictionary.get(ch, 0)+1

for key,value in dictionary.items():
    output += (str(value)+key)

print(output)

# hard way
string = 'abaabbca'
string = ''.join(sorted(string))

count = 0
output = ''
s = string[0]

for ch in string:
    if ch == s[0]: count += 1
    else:
        output += str(count) + s
        s = ch
        count = 1

if s == string[-1]:
    output += str(count)+s


print(output)
