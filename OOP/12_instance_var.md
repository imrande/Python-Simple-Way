## How to access instance variables

- within class, we can access instance variables by using self.
- outside class we can access variables with the help of reference variable.

```py
class Test:
	def __init__(self):
		self.a = 10
		self.b = 20

	def displayVariables(self):
		print(self.a) # 10 => insie class
		print(self.b) # 20

test = Test()
test.displayVariables()
print(test.a) # 10 => outside class
```

## How to delete instance variables

- within class by using self
	- del self.variableName
- outside class by using help of reference variable
	- del referenceObject.variableName

```py
class Test:
	def __init__(self):
		self.a = 10
		self.b = 20
		self.c = 30
		self.d = 40

	def m1(self):
		del self.c # inside class

test = Test()
print(test.__dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
test.m1()
print(test.__dict__) # {'a': 10, 'b': 20,'d': 40}
del test.a # outside class
print(test.__dict__) # {'b': 20,'d': 40}
test2 = Test()
print(test2.__dict__) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
```

## How to update instance variables

- if we change the values of instance variables of one object, then those changes won't be reflected to other objects, because for every object a separate copy of instance variables are available...

```py
class Test(object):
	"""docstring for Test"""
	def __init__(self):
		self.a = 10
		self.b = 20

t1 = Test()
t1.a = 888
t1.b = 999

t2 = Test()
print(t1.a, t2.a) # 888 10
print(t2.b, t1.b) # 20 999
```
