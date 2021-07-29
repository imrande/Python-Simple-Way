# global keyword uses
# Make local variable value as available to all function scope
a = 5
def f1():
	global a
	a = 10
	print(a) # => 10

def f2():
	print(a) # => before global a is 5
	print(a) # => after global a is 10

# Declare global variable inside function
def f11():
	global a
	a = 20
	print(a) # => 20

def f22():
	print(a) # => before global a NameError
	print(a) # => after global a is 20

aa = 777
def f(): # SyntaxError
	print(aa) # => 777
	global aa # it should be first line in function scope
	aa = 999
	print(aa) # => 999

f()

# Correct version
aa = 777
def f(): 
	global aa
	print(aa) # => 777
	aa = 999
	print(aa) # => 999

f()

# by default globals() function contains all global vars in module
# how to access global vars inside function scope when local var is available
a = 888
def ff():
	a = 999
	print(a) # => 999
	print(globals().get('a')) # return dict => 888

ff()