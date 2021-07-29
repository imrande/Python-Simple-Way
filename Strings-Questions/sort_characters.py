# sort characters the string, first alphabets followed by digits

string = input()

sorted_str = ''.join(sorted(string))
alphabets = ''
digits = ''

for i in sorted_str:
    if i.isalpha(): alphabets += i
    elif i.isdigit(): digits += i

print(alphabets + digits)