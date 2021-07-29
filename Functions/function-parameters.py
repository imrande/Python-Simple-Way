# Function for accept 2 paras and return sum

def Addition(a, b):
	return a+b

print(Addition(10, 20)) # => 30
assert Addition(10, 20) == 30

# Print factorial of postive n number
def factorial(n):
	if n > 1:
		return factorial(n-1)*n
	return 1

print(factorial(3)) # => 6
print(factorial(4)) # => 24

for i in range(1, 6): 
	print(f'The factorial of {i} is {factorial(i)}')