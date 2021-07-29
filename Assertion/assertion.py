# https://wiki.python.org/moin/UsingAssertionsEffectively
# https://dbader.org/blog/python-assert-tutorial

# The process of identifying & fixing errors(bug) are called debugging...

# Main advantage of assertion over print() statement is we can enable/disable as our requirement. Don't need to delete explicitly
# by default assert is enable, for disable --> "python -O File"

# there are 2 types of assertion 
	# simple version
		# assert conditional_statement
	# augmented version
		# assert conditional_statement, 'message'

# def squre(x): return x**x
def squre(x): return x*x

assert squre(2) == 4
assert squre(3) == 9 # raise AssertionError
assert squre(4) == 16

print(squre(2)) # 4 -> got 4
print(squre(3)) # 9 -> got 27
print(squre(4)) # 16 -> got 256