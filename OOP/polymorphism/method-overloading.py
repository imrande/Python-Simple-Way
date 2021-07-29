# two methods are said to be overloaded if both methods having same name, but different args types...
# method and constructor overloading doesn't support python... 
# since python is dynamically type and it's no concept explicit type like c++ has
# If we declare 2 methods with same name python will consider most recent method

class TestSample():
	def m1(self):
		print('no-args')

	def m1(self, x):
		print(x)

t = TestSample()
t.m1(50) # -> 50

# we can implement overloading concept in python 2 ways(not really require)
# set all args default value is None and explicit condition check...
# variable argument count

class Test:
	def __init__(self, *args):
		self.args = args

	def getProduct(self):
		total = 1
		for i in self.args: total *= i
		return total

t = Test(2, 5, 7)
print(t.getProduct())