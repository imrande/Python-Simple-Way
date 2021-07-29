from functools import wraps

def bold(func):
	"""Bold decorator"""
	@wraps(func)
	def wrapper():
		"""return html bold tag"""
		result = f'<b>{func()}</b>'
		return result
	return wrapper

def italic(func):
	"""Italic decorator"""
	@wraps(func)
	def wrapper():
		"""return html italic tag"""
		result = f'<i>{func()}</i>'
		return result
	return wrapper

@bold
@italic
def printfib():
	"""return Fibonacci"""
	return "Fibonacci"

print(printfib())

print(printfib.__name__) # printfib
print(printfib.__doc__) # return Fibonacci