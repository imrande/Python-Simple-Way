# Demo 3
def invitation(func):
	def processing(name):
		names = ('Narenda Modi', 'Boris Johnson')
		if name in names:
			print(f'Hello {name}, Thank you for giving us time')
			print('You are very important to us')
		else: func(name)
	return processing

@invitation
def wish(name):
	print(f'{name}, thanks for coming')

wish('Durga')
wish('Boris Johnson')

# Demo 4
def catchError(func):
	def fixError(a, b):
		if b == 0:
			print('Please provide any value > 0')
		else: func(a, b)
	return fixError

@catchError
def division(a, b): print(a / b)

division(10, 2)
division(10, 0)