# calculate time for fibonacci call

from time import perf_counter
from functools import wraps, lru_cache

def timer(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		end = perf_counter()
		duration = end - start
		arg = str(*args) # '(n)'
		print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}')
		return result
	return wrapper
		
@timer
def fib(n):
	"""return nth value from fibonacci sequence"""
	if n < 2:
		return n
	return fib(n-2) + fib(n-1)

fib(15) # it takes long time for call

# Efficient version
def timer2(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		end = perf_counter()
		duration = end - start
		arg = str(*args) # '(n)'
		print(f'{func.__name__}({arg}) = {result} -> {duration:.8f}')
		return result
	return wrapper
	
@lru_cache(maxsize=None)	
@timer2
def fib2(n):
	"""return nth value from fibonacci sequence"""
	if n < 2:
		return n
	return fib2(n-2) + fib2(n-1)

fib2(15)