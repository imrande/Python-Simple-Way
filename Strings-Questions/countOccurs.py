# program to find number of occurrences of each character present in the given string with count() method

# if input is '' then it will return nothing after complete program
s = input() 
unique = ""

for ch in s: # O(n)
    if ch not in unique:
        unique += ch

for ch in unique: # O(n)
    print(f'{ch} occurs {s.count(ch)} times')

# time complexity of above program is O(n) and space complexity is O(1)

# 2nd way
s1 = input()
u = ''.join(set(s1))

for ch in u:
    print(f'{ch} occurs {s1.count(ch)} times')

# time O(n) and space O(1)