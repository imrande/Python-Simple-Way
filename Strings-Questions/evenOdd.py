# write a program for character present at even & odd index separately

string = input()

print('Character present at even index:')
for i in range(0, len(string),2):
    print(string[i])

print('Character present at odd index:')
for i in range(1, len(string),2):
    print(string[i])

# slice operator
print('Character present at even index:')
print(string[::2])

print('Character present at odd index:')
print(string[1::2])