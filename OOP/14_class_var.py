# Access class variables

# inside constructor/instance method by using `ClassName or self`
# inside class method by using cls or className
# inside static method by using class name
# outside class either objReference or className

class Test:
	a = 20

	def __init__(self):
		print(self.a) # 20
		print(Test.a) # 20

	@classmethod
	def classMethod(cls):
		print(Test.a)
		print(cls.a)

	@staticmethod
	def staticMethod():
		print(Test.a)  # 20

t = Test()
print(t.a) # 20
print(Test.a) # 20
t.staticMethod()
Test.a = 200000
t.classMethod() # 200000 -> 200000