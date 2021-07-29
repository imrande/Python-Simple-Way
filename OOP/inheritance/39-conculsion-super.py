# From child class constructor and instance methods, we can call parent class
# constructors, instance methodds, class methods, static methods by using super()

# From child class, inside class method we can't access parent class
# constructor & instance variables(they are associated with objects) 
# directly by using super()... but we can acess class and static methods...
# by using super() or className

# From child class, inside static method we can't use super() to call parent class members...but we can call (class and static methods) by className
# static method has no relation with eiter object or class

class P:
	@classmethod
	def m2(cls):
		print('Parent class method')

	@staticmethod
	def m3():
		print('Parent static method')

class C(P):
	@staticmethod
	def m2():
		P.m2()
		P.m3()

c = C()
c.m2()