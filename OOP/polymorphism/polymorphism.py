# One name but multiple form is called polymorphism

# Polymorphism concepts
# 1. Overloading
	# Operator overloading
	# Method overloading
	# Constructor overloading
# 2. Overriding
	# Method overriding
	# Constructor overriding
# 3. Pythonic Behavior:
	# Duck typing
	# Monkey patching
	# Easier to ask forgiveness than permission(EAFP)

# Example
print(10 + 20) # -> 30
print('10 ' * 3) # -> 10 10 10

class Parent:
	def marry(self):
		pass

class Child(Parent):
	def marry(self):
		print('Azeri girl')

child = Child()
child.marry()