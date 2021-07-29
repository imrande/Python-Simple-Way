# how to call method of a particular super class
# we can't use super() to access parent class instance variables from child
# class.. We should use self only...
class A:
	def m1(self): 
		print('A class method')

class B(A):
	def m1(self):
		print('B Class method')

class C(B):
	def m1(self):
		print('C Class method')

class D(C):
	def m1(self):
		print('D class method')

class E(D):
	def m1(self):
		super().m1() # invoked immediate parent class
		# jump any particular class
		B.m1(self) # -> B class method
		# 2nd way
		super(B, self).m1() # -> A class method

e = E()
e.m1()