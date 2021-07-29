class Customer:
	"""docstring for customer"""
	bank_name = 'City Bank'

	def __init__(self, name, balance=0.0):
		self.name = name
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print(f'After deposit new balance is {self.balance}')

	def check_balance(self):
		bal = f'Your current balance is {self.balance}'
		return bal

	def withdraw(self, amount):
		if amount > self.balance:
			print('Insufficient fund')
		else:
			self.balance -= amount
			print(f'After withdraw new balance is {self.balance}')

print(f'Welcome to {Customer.bank_name}')
print('d - deposit')
print('w - withdraw')
print('c - check balance')
print('e - exit')
print('_ _ _ _ _ _ _ _ _ _')
print()

name = input('Please, Provide our your name ')
customer45 = Customer(name)

while True:
	option = input('Choose option ').lower()

	if option in ['d', 'e', 'c', 'w']:
		if option == 'd':
			amount = float(input('Amount you want to deposit '))
			customer45.deposit(amount)

		elif option == 'e':
			print('Thank you for online banking')
			break

		elif option == 'c':
			print(customer45.check_balance())

		elif option == 'w':
			amount = int(input('Amount you want to withdraw '))
			customer45.withdraw(amount)
	else:
		print('Invalid request, try again!!')