# Types of variable in python oop

3 types of variables are allowed in python OOP

- instance variable
- class variable
- local variable

## Instance variable

- If the value of variable is varied from object to object such kind of variables are called instance variables.
- For every object a separate copy of instance variable will be created.
- It is declared inside python constructor

## Class variable

- If the value of variable is not varied from object to object such kind of variables are called static variables.
- For every class only one static variable will be created and shared by every objects.
- It should be declared inside python class

## Local variable

- If the variable is declared inside a method for temporary requirement such variables are called local variable.

```py
class Test:
	university_name = 'Southeast University' # class variable 'university_name'
 
	def __init__(self, name): # local variable 'name'
		self.name = name # instance variable 'self.name'

	def myInfo(self):
		return (f'My name is {self.name}\n'
		f'My university name is {Test.university_name}'
		)

test = Test('Imran')
print(test.university_name) # Southeast University
print(test.myInfo()) # Name=Imran, University=Southeast University

```
