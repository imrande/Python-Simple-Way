# when group of statement repeatedly require then best is put statements inside function...
# Main advantage is code reuse-ability...

def Calculate(a, b):
	print(f'The sum {a+b}')
	print(f'The difference {b-a}')
	print(f'The product {a*b}')

Calculate(10, 20)
Calculate(100, 200)
Calculate(1000, 2000)

# 2 types of function is available in python
	# built in function (id(), eval(), len())
	# user defined function

# write a function to print wish message
def wish(): 
	print('Hello Friends, Good Evening!!')

wish()