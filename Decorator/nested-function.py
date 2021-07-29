# when a function is declared inside another function is called nested function...
# nested function can't be invoked from outside of inner function

def outer():
	print('Outer function execution started')
	def inner(): print('Inner function execution')
	inner()
	print('Outer function execution completed')

outer()