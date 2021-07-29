# print diamond pattern n number of times with * symbols
number_of_times = int(input('Number of rows: '))

for i in range(1, number_of_times + 1):
    print(' ' * (number_of_times-i) + '* ' * (i))

print(end='')
for i in range(1, number_of_times):
    print(' ' * i + '* ' * (number_of_times-i))