from make_posh import make_posh, pfib
from functools import wraps

def make_posh(func):
	"""Function decorator"""
	@wraps(func) # solution of this problem
	def wrapper():
		"""Wrapper function"""
		print('+---------+')
		print('|         |')
		print(f'{func()}')
		print('|         |')
		print('+=========+')
	return wrapper

@make_posh
def pfib():
	"""print out fibonacci"""
	return ' Fibonacci'

# when we call module as decorator function, its return decorated(inner ) function,rather than itself
# print(pfib.__name__) => wrapper
# print(pfib.__doc__) => Wrapper function

print(pfib.__name__) # pfib
print(pfib.__doc__) # print out fibonacci