from functools import wraps

def munch(start, end):
	def do_munch(func):
		"""replace character decorator"""
		@wraps(func)
		def wrapper(*args, **kwargs):
			new_str = ''
			result_str = func(*args, **kwargs)

			for index, char in enumerate(result_str):
				c = 'x' if start <= index < end else char
				new_str += c
			return new_str
		return wrapper
	return do_munch

@munch(1, 4)
def replaceStr():
	return "Fibonacci"

print(replaceStr()) # Fxxxnacci