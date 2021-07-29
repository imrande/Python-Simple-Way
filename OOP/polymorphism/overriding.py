"""
What ever members available in the parent class are by default available to the child class through inheritance. If the child class is not satisfied with parent class implementation then child class is allowed to redefine that method in the child class based on its requirement. This concept is called overriding.
Overriding concept applicable for both methods and constructors.
"""

class Parent:
	def property(self):
		return 'Love ❤️‍🔥'

	# method overridden
	def marriage(self):
		print('Random girl')

class Child(Parent):
	# method overriding
	def marriage(self):
		print('Azeri Girl 😏')

child = Child()
child.marriage()

# Constructor
class DemoClass:
	# overridden
	def __init__(self):
		print('DemoClass constructor')

class DemoChildClass(DemoClass):
	# overriding
	def __init__(self):
		print('DemoChildClass constructor')

demo = DemoChildClass()