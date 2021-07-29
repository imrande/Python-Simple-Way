# our internal data should not go out directly...outside person can't access direct way, 
# this is called data hiding. we can implement it via private attribute..
# Main advantage is security....
# we can access private method/variable only inside class...
# private conversion is __variable/method Name

class Test:
	def __init__(self):
		self.__x = 50

	def __m1(self):
		print('Private method')

	def m2(self):
		self.__m1()
		print(self.__x)

t = Test()
t.m2()
# by default we can't access private method/variables from outside but 
# we can access them other way (objectRef._className__var/method) [it's called name mangling]
# t.__x -> AttributeError
print(t._Test__x) # -> 50
t._Test__m1() # -> private method