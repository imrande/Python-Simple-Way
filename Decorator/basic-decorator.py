# Decorator is a function which can take another function as arguments and
# extend its functionality and returns modified function with extended functionality

# Main objective of decorator is we can extend functionality of existing function without modifying the original function

def decorating(funArgs):
	def inner():
		print('Send the person to Beauty Parlor')
	return inner
	# return funArgs => showing a person ...

@decorating
def display():
	print('Showing a person as it is')

display()

# Demo 2
def addInts(func):
	def calcuating(a, b):
		return sum((a, b))
	return calcuating

@addInts
def add(a, b): pass
print(add(10, 20))

# Demo 2.x

def addition(func):
	def calcuation(a, b):
		print('#' * 15)
		print(f'The sum is {func(a, b)}')
		print('#' * 15)
	return calcuation

@addition
def addValue(a, b): return a+b
addValue(10, 20)