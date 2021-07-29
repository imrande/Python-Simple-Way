# We can define multiple decorators for the same function and all these decorators will form Decorator Chaining

# Demo 1
def decorator_1(func):
	def inner():
		print('decorator_1 execution')
	return inner 

def decorator_2(func):
	def inner():
		print('decorator_2 execution')
	return inner 

## it will take arg from return value of @decorator_1
# which is inner and finally decorator_2's inner() is called
@decorator_2 
@decorator_1 # it will take argument func() and retrun inner object function
def func():
	pass

func()

# Extend Demo 1
def decorator_11(func):
	def inner():
		print('decorator_11 execution') # 2
		func()
	return inner 

def decorator_22(func):
	def inner():
		print('decorator_22 execution') # 1
		func()
	return inner 

## it will take arg from return value of @decorator_1
# which is inner and finally decorator_2's inner() is called
@decorator_22 
@decorator_11 # it will take argument func() and retrun inner object function
def func2():
	print('Original function') # 3

func2()

# Extend Demo 1.x
def decorator_13(func):
	def inner():
		print('decorator_13 execution')
		func()
	return inner 

def decorator_23(func):
	def inner():
		print('decorator_23 execution') # 1
		# func3() => it will start from scratch (recursion)
	return inner 

@decorator_23 
@decorator_13
def func3():
	print('Original function')

func3()
print() # new link

# Demo 2
def dec(func):
	def inner():
		x = func()
		return x * x
	return inner

@dec
def squareNumber():
	return 20

print(squareNumber()) # => 400

# Extend Demo 2
def numberDouble(func):
	def inner():
		x = func()
		return x * x
	return inner

def squareNumber(func):
	"""squre number"""
	def inner():
		x = func()
		return 2 * x
	return inner

@squareNumber
@numberDouble
def squareNumber2():
	return 20

print(squareNumber2()) # => 800