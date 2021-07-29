# how to use try with multiple except block

try:
    with open('abc.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)

# 2nd example
try:
    number = 10
    number_2 = 'two'
    print(number / number_2)
# order is important for exception
except ZeroDivisionError as e:
    print(e)
except ValueError as v:
    print(v)
except TypeError as t:
    print(t)
    
# 3rd example
try:
	print( 10 / 0)
except ArithmeticError as arithmetic:
	print('arithmetic')
except ZeroDivisionError as zero:
	print('zero')