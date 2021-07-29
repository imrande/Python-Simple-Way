# write a program to reverse the internal content of each word

string = input().split()
new_list = []

for i in string:
    new_list.append(i[::-1])

print(' '.join(new_list))

# One linear
string2 = input().split()
new_str2 = [i[::-1] for i in string2]
print(' '.join(new_str2))