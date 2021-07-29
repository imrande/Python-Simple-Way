class P:
	def m1(self): print('Parent class method')

class C(P):
	def m2(self):
		super().m1() # best practice
		# P.m1(self) [kinda silly]
		print('child class methid')

c = C()
c.m2() # -> parent class method -> child class method
print() # blank line

# ========================
class Parent:
	a = 10

	def __init__(self): print('Parent Constructor')

	def m1(self): print('Parent Instance method')

	@classmethod
	def m2(cls): print('Parent class method')

	@staticmethod
	def m3(): print('Parent static method')

class Child(Parent):
	def __init__(self):
		print('Child Constructor')

	def method(self):
		print(super().a) # -> 10
		super().m1() # -> parent Instance method
		super().m2() # -> parent class method
		super().m3() # -> parent static method
		super().__init__()
		# super().Parent() -> Error

child = Child()
child.method()