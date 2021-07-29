# How to delcare instance variables

# 3 places we can declare instance variable
# 1) inside constructor by using self
# 2) inside instance method by using self
# 3) outside of class with help of reference variable

class Test:
	"""docstring for test"""
	def __init__(self):
		self.x = 10 # 1
		self.y = 20

	def m1(self): # it won't be added to object until it get invoked
		self.z = 30 # 2

# number of instance variable are varied from object to object
t = Test()
print(t.__dict__) # {'x': 10, 'y': 20}
t.m1()
print(t.__dict__) # {'x': 10, 'y': 20, 'z': 30}

t2 = Test()
print(t2.__dict__) # {'x': 10, 'y': 20}
t2.c = 50 # 3
print(t2.__dict__) # {'x': 10, 'y': 20, 'c': 50}