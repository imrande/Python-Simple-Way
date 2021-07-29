# The process of binding data members and attributes into a single unit is called encapsulation.
# hiding data behind members is the main idea of encapsulation
# Every python class is an example of encapsulation...

class Student:
	data members/behaviors :- read(),walk() 
	attributes/variables :- id, mark, name

# If any component follows data hiding and abstraction, such type of components is called encapsulation component
# Component == data hiding + abstraction

class Account:
	def __init__(self, balance): self.__balance = balance
	def getBalance(self): return self.__balance
	def deposite(self, amount): self.__balance += amount
	def withdraw(self, amount):
		if amount < self.__balance and self.__balance > 0:
			self.__balance -= amount

# Advantages :-
# Security
# Maintainability, Modularity
# Modification easy