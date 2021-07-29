# Inheritance types in python

- single inheritance
- multi level inheritance
- multiple inheritance
- hierarchical inheritance
- cyclic inheritance
- hybrid inheritance

## Single Inheritance

The concept of inheriting members from one class to another class is known as single inheritance... (single parent and single class)

```py
class Parent:
	def method1(self):
		print('parent class method')

class Child(Parent):
	def method2(self):
		print('child class method')

child = Child()
child.method1() # -> parent class method
child.method2() # -> child class method
```

## Multi level Inheritance

The concept of inheriting members from multiple classes to single class with the concept of one after another is known as multi level inheritance...(grand parent -> parent -> child)

```py
class GrandParent:
	def method1(self):
		print('Grand Parent class method')

class Parent(GrandParent):
	def method2(self):
		print('parent class method')

class Child(Parent):
	def method3(self):
		print('child class method')

child = Child()
child.method1() # -> Grand Parent class method
child.method2() # -> parent class method
child.method3() # -> child class method
```

## Hierarchical Inheritance

The concept of inheriting members from one class to multple classes which present at the same level is known as hierarchical inheritance...(parent -> multple child)

```py
class Parent:
	def method1(self):
		print('parent class method')

class Son1(Parent):
	def method2(self):
		print('child1 class method')

class Son2(Parent):
	def method3(self):
		print('child2 class method')

child = Son1()
child.method1() # -> parent class method
child.method2() # -> child1 class method

child2 = Son2()
child2.method1() # -> parent class method
child2.method3() # -> child2 class method
```

## Multiple Inheritance

The concept of inheriting members from multiple classes to a single class at a time is known as multiple inheritance... (one child -> multiple parents)

```py
class Parent:
	def method1(self):
		print('parent class method')

class FosterParent():
	def method2(self):
		print('foster parent class method')

class Son(Parent, FosterParent): # order is important
	def method3(self):
		print('child class method')

son = Son()
son.method1() # -> parent class method
son.method2() # -> foster parent class method
```

## Hybrid Inheritance

Combination of single, multiple, multi level, hierarchy inheritance. It is followed MRO... `print(className.mro())`

## Cyclic Inheritance

It doesn't support in Python...