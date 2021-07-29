# delete class variables

# we can delete class variables inside either cls or className and outside className...
# we can't modify class variables inside class by `self` and outside `object reference variable`

class Test:
	a = 10

	@classmethod
	def m1(cls):
		del Test.a
		# dele cls.a

Test.m1()
Test.a = 2000
print(Test.__dict__)
del Test.a
print(Test.__dict__)
print()

# ===============================
class Test2:
	a = 10
	def __init__(self):
		Test2.b = 20
		del Test2.a

	def m1(self):
		Test2.c = 10
		del Test2.b

	@classmethod
	def m2(cls):
		cls.d = 40
		del Test2.c

	@staticmethod
	def m3():
		Test2.e = 50
		del Test2.d

t1 = Test2()
t1.m1()
Test2.m2()
Test2.m3()
# del Test2.e
print(Test2.__dict__) # {'e': 50}