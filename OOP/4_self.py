# postmortem of self

# `self` is a ref variable which is always pointing to current object.
# It is used to reference the obj inside the class.
# main purpose of self is to declare & access instance variable.
# `self` is not a keyword in python. we can use any word instead of `self`. but self is recommanded.
# first argument of constructor and instance method is always self
# self can't be used outside of class

class Test(object):
	"""docstring for Test"""
	def __init__(self):
		print(f'Address of the object pointed by self {id(self)}') # same as ref variable (t)

t = Test()
print(f'Address of object pointed by ref variable {id(t)}') # same as self

# since self is not keyword in python, we can use anything instead self
class Student:
	"""docstring for Student"""
	def __init__(delf, name, id, mark):
		delf.name = name
		delf.id = id
		delf.mark = mark

	def Name(kelf):
		return kelf.name

student = Student('bunny', 101, 96)
print(student.Name()) # bunny