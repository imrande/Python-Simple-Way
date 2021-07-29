# Example 01

class Test:
	a = 10
	def m1(self):
		self.a = 888

t1 = Test()
t1.m1()
print(Test.a) # 10
print(t1.a) # 888
print()

# Example 02

class Test2:
	a = 10
	def m1(self):
		Test2.a = 8888

t1 = Test2()
t1.m1()
print(Test2.a) # 8888
print(t1.a) # 888
print()

# Example 03

class Test3:
	a = 10
	def __init__(self):
		self.b = 20

t1 = Test3()
t2 = Test3()
print('t1', t1.a, t1.b) # 10 20
print('t2', t2.a, t2.b) # 10 20

t1.a = 888
t1.b = 999
print('t1', t1.a, t1.b) # 888 999
print('t2', t2.a, t2.b) # 10 20
print()

# Example 04

class Test5:
	a = 10
	def __init__(self):
		self.b = 20

t1 = Test5()
t2 = Test5()

print('t1 ->', t1.a, t1.b) # 10 20
print('t2 ->', t2.a, t2.b) # 10 20

Test5.a = 888
Test5.b = 999
print('t1 ->', t1.a, t1.b) # 888 20
print('t2 ->', t2.a, t2.b) # 888 20
print('Test5 ->', Test5.a, Test5.b) # 888 999
print()

# Example 05

class A:
	a = 10
	def __init__(self):
		self.b = 20

t1 = A()
t2 = A()
A.a = 888
t1.b = 999

print('t1', t1.a, t1.b) # 888 999 
print('t2', t2.a, t2.b) # 888 20
print()

# Example 06

class A2:
	a = 10
	def __init__(self):
		self.b = 20

	def m1(self):
		self.a = 888
		self.b = 999

t1 = A2()
t2 = A2()
t1.m1()

print('t1', t1.a, t1.b) # 888 999 
print('t2', t2.a, t2.b) # 10 20
print()

# Example 07

class B:
	a = 10
	def __init__(self):
		self.b = 20

	def m1(self):
		self.a = 888
		self.b = 999

t1 = B()
t2 = B()
t1.m1()
t2.m1()
print('t1', t1.a, t1.b) # 888 999 
print('t2', t2.a, t2.b) # 888 999
print()

# Example 08

class B2:
	a = 10
	def __init__(self):
		self.b = 20

	@classmethod
	def m1(cls):
		cls.a = 888
		cls.b = 999

t1 = B2()
t2 = B2()
t1.m1()
print('t1', t1.a, t1.b) # 888 20 
print('t2', t2.a, t2.b) # 888 20
print('B2 ->', B2.a, B2.b) # 888 999
print()