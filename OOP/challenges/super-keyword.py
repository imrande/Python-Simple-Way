# State use of super keyword using example

# 2 cases where we can use super() in python program
	# call the __init__() method of base class
	# call the methods/attributes of base class

class A:
	def __init__(self, x):
		self.a = x
	def display(self):
		print(self.a)

class B(A):
	def __init__(self, x, y):
		super().__init__(x)
		self.b = y

	def display(self):
		super().display()
		print(self.b)

b = B(10, 20)
b.display()