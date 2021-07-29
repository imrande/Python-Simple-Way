number_of_times = int(input('Enter number of rows: '))

# print * symbol n number of times
print(number_of_times * '* ')


# Print square pattern n number of times with * symbols
for _ in range(number_of_times):
    print('* ' * number_of_times)


# print square pattern with provided fixed digit in every row
for i in range(1, number_of_times+1):
    print((str(i)+' ') * number_of_times)


# print square pattern with alphabet symbol
number_of_times = 5
for i in range(number_of_times):
    print((chr(65+i) +' ') * number_of_times)