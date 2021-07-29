# Implement a Banking Account using the concepts of inheritance.

class Account:
	def __init__(self, title=None, balance=0):
		self.title = title
		self.balance = balance

class SavingsAccount(Account):
	def __init__(self, title=None, balance=0, interestRate=0):
		super().__init__(title, balance)
		self.interestRate = interestRate

account = Account('Mark', 5000)
