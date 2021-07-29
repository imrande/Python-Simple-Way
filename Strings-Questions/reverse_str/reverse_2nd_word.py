# write a program to reverse internal content of every second word present in a given string

string = input().split()

# one linear
new_str = ' '.join(string[i][::-1] if i % 2 != 0 else string[i] for i in range(len(string)))
print(new_str)