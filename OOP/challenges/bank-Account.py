"""
The parent class contains the general information about an account and an
abstract method to calculate the yearly interest. For savings account, the interest rate is 10% and for current account the interest rate is 6%. All the data members of the Account class are initialized through a parameterized constructor. Your program should be able to deposit and withdraw money from a saving account. Perform the same operation on a current account
"""

from abc import ABC, abstractmethod

class Account(ABC):
	def __init__(self, account_no, balance=0):
		self.account_no = account_no
		self.balance = balance

	@abstractmethod
	def yearly_interest(self, rate):
		pass

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance < amount and self.balance > 0:
			self.balance -= amount
		else:
			print('Insufficient Funds')

class SavingAccount(Account):
	def __init__(self, account_no, balance):
		super().__init__(account_no, balance)

	def yearly_interest(self, rate):
		self.balance += (self.balance * rate) // 100

class CurrentAccount(Account):
	def __init__(self, account_no, balance):
		super().__init__(account_no, balance)

	def yearly_interest(self, rate):
		self.balance += (self.balance * rate) // 100

user_1 = SavingAccount(1001, 5000)
user_1.deposit(1000)
user_1.yearly_interest(10)
user_1.withdraw(500)

user_2 = CurrentAccount(100001, 5000)
user_2.deposit(1000)
user_2.yearly_interest(6)
user_2.withdraw(500)