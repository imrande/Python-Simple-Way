from functools import reduce
x = ['Hello ', 'World']
print(reduce(lambda x, y: x+y, x))

# sum of first 100 numbers
sumOfNumbers = reduce(lambda x, y: x+y, range(1, 101))
print(sumOfNumbers)
