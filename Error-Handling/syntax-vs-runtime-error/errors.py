# There is only 2 types of error
	# Syntax Error -> Invalid syntax
	# Runtime Error -> (ZeroDivisionError, ValueError, TypeError)

# syntax error => which occurs because of invalid syntax (grammar)
# 1st example
print "hello" # SyntaxError

# 2nd example
x = 10
if x == 10
    print(x)

# runtime error => while executing the program at runtime if something goes
# wrong because of invalid userInput, memory problem, wrong logic etc then we 
# will get runtime error...(ZeroDivisionError, ValueError, ArithmeticError etc)
# RUntime errors known as exception...

# if user give input incorrect value it will arise (ValueError/ZeroDivisionError)
number_1 = int(input('Enter number: '))
number_2 = int(input('Enter another: '))
print(number_1 // number_2)

# 2nd example
file = open('xyz.txt', 'r')
print(file.read()) # FileNotFoundError
file.close()
