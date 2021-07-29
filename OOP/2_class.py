# how to define a class

class Student:
	"""documentation string"""
	pass

# create object
rani = Student()

# print the doc string
print(Student.__doc__)
print(rani.__doc__)

# print class information
print(help(Student))

# 3 types of variables are allowed in python class
	# instance variable (object level variable)
	# class variable (class level variable)
	# local varialbe (method level varialbe)

# 3 types of methods are allowed in python class
	# instace method
	# static method
	# class method