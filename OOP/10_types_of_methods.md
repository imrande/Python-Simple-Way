# Types of method in Python oop

3 types of methods available in python

- static method
- instance method
- class method

## Static Method

- Inside a class if we declare a method which has no relation or reference with class or instance variable, we can call it static methods.
- Decorator @staticmethod is required

## Class Method

- Inside a method if we're using only class variables not any instance variable, then we can call it class methods.
- Decorator @classmethod is required
- First argument is always cls, which is refer to class object
- For every class one special object will be created by PVM to maintain class level variables, which is called class level object. cls is the reference variable to pointtng to that object.

## Instance Method

- Inside a method if we're trying to access instance variables we can call it instance variable.
- No decorator is required
- First argument is always self, which is refers to particular object.

```py
class Student:

	university_name = 'Telusko University'

	def __init__(self, name):
		self.name = name

	@classmethod
	def get_student_info(cls):
		return cls.university_name

	@staticmethod
	def get_location():
		return 'Mohammadpur, Dhaka-1207'

student = Student('Imran')
print(student.get_location())
print(student.get_student_info())

```