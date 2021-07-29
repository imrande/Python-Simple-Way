# Beautify the output

def make_posh(func):
	"""Function decorator"""
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

if __name__ == '__main__':
	pfib()
	print(pfib.__name__) # wrapper
	print(pfib.__doc__) # wrapper function
