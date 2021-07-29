# program to find number of occurrences in a given string with dict

s = input()
d = dict()

for ch in s:
    d[ch] = d.get(ch, 0)+1 # if the key is available in d then it will count occurs by 1 and if not then set 1

for ch, o in d.items():
    print(f'{ch} occurs {o} times')