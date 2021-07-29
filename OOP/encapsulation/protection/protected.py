# we can access protected variable/method inside class and child class only...
# protected convension is _variable/method Name

class Test:
	def __init__(self):
		self._x = 5

class SubTest(Test):
	def m2(self):
		print(self._x)

t = SubTest()
t.m2() # -> 5
# python officially doesn't provide protected,private technique...It's just naming convension for programmer...
print(t._x) # -> 5