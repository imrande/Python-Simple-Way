# Various places we can declare class variables :=

# * within the class directly but outside of constructor or method
# * inside instance method by using `className`
# * inside class method by using `cls` / className
# * inside static method by using `className`
# * inside constructor by using `className`
# * outside of the class by using `className`

class Test:
	a = 10 # inside class
	def __init__(self):
		self.x = 55 # instance variable
		Test.b = 20 # class variable

	def instanceMethod(self):
		print(self.a) # access class variable value
		Test.c = 30 # class variable

	@classmethod
	def clsMethod(cls):
		cls.g = 70 # class variable
		Test.d = 40 # class variable

	@staticmethod
	def staticMethod():
		Test.e = 50 # class variable

t = Test()
t.instanceMethod()
Test.clsMethod()
T.staticMethod()
Test.f = 60 # outside class variable
print(Test.__dict__) # it will print all class related info

t1 = Test()
print(Test.__dict__) # one copy of cls vars