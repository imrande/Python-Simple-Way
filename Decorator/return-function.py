# Function can return another function

def outer():
	def inner(): print('Inner function')
	return inner # return inner object

outer_ = outer() # catch inner function object, which will assign to outer_
outer_()

# difference between f1 = outer and f1 = outer()
# f1 and outer both pointing to same object, function aliasing
# outer() returned something which will assign to f1, function call