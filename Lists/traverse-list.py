# using while loop
l = list(range(11))
while len(l) > 0:
	print(l.pop())

# using enumerate
for index, value in enumerate(range(11)):
	print(index, value)

# using for loop
for i in range(11):
	print(f'{i} ', end='')
print()
