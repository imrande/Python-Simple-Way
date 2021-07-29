numberOfTimes = int(input('Enter number of rows: '))

# print pyramid pattern n number of times with * symbols
for i in range(1, numberOfTimes + 1):
    print((' ')*(numberOfTimes - i) + i*'* ')


# print invarted pyramid pattern n number of times with * symbols
for i in range(1, numberOfTimes+1):
    print((' ')*(i-1) + '* ' * (numberOfTimes - i +1))