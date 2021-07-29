# program to find number of occurrences each vowel present in the given string

string = input()
x = ''.join(set(string))

for ch in x:
    if ch in 'aeiou':
        print(f'{ch} occurs {string.count(ch)} times')

# with dict
string2 = input()
d = {}

for ch in string2:
    if ch.lower() in 'aeiou':
        d[ch] = d.get(ch, 0) + 1

for key,value in d.items():
    print(f'{key} occurs {value} times')