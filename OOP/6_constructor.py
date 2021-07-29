# full story of constructor

# the main purpose of constructor/__init__ is to declare & initialize instance variable.
# in Python constructor is optional, if we don't declare __init__() methd, python provide it by default.
# constructor is a special method
# name of the constructor is always is __init__()
# we aren't required to call constructor explicitly. whenever object is created the constructor will be executed implicitly.
# per object constructor will be executed only one.
# constructor can take any number arg but at least one(self) should be per obj
# overloading is not possible in constructor
# explicit constructor exceuted just like normal method

class Test:
	def __init__(self):
		print('Constructor execution')

t1 = Test() # 1st time print (constructor execution)
t2 = Test() # 2nd time print (constructor execution)
t3 = Test() # 3rd time print (constructor execution)

class Test2:
	def __init__(self, name):
		self.name = name

	def Name(self):
		return self.name

test2 = Test2('Rena') # implicit constructor call and one object is created
print(test2.Name()) # Rena

test2.__init__('c') # explicit constructor call but it won't create new obj &
test2.__init__('b') # behaving like normal method
test2.__init__('a')
print(test2) # object location in memory
print(test2.Name()) # a

# method overloading is not possible in python
class Constructor(object):
	def __init__(self):
		print('Method Overloading')

	# PVM only consider the most recent method, if there are 2/3/4 methods with same name.
	def __init__(self, name):
		self.name = name

	def Name(self): 
		return self.name

constructor = Constructor('Alina')
print(constructor.Name()) # Alina