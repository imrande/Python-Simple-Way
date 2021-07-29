# Modify class varialbes

# we can modify class variables anywhere (inside or outside) in the class. Inside class 'class' variable can be modified only cls or className, not self... 
# outside class 'class' variable can be modified only className, not object reference variable. 

class Test:
	"""docstring for test"""
	a = 10
	def __init__(self):
		Test.a = 20 

	def m1(self):
		Test.a = 30

	@classmethod
	def m2(cls):
		cls.a = 40
		Test.a = 50

	@staticmethod
	def m3():
		Test.a = 60

t = Test()
Test.a = 70
# del Test.a
print(t.a)