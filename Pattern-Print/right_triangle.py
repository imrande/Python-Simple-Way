numberOfTimes = int(input('Enter number of rows: '))

# print right triangle pattern with * symbols
for i in range(1, numberOfTimes + 1):
    print('* ' * i)

# print Inverted right triangle pattern with * symbols
numberOfTimes = 5
for i in range(1, numberOfTimes + 1):
    print('* ' * (numberOfTimes-i+1))