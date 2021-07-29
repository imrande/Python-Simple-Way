# demo of a class

class Student:
	"""docstring for Student"""
	def __init__(self):
		self.name = "durga"
		self.id = 101
		self.mark = 90

	def talk(self):
		print(f'Hello, My name is {self.name}')
		print(f'My id is {self.id}')
		print(f'My mark is {self.mark}')

s = Student()
print(s.name) # durga
print(s.id) # 101
print(s.mark) # 90
s.talk()

# best practice
class StudentInfo():
	"""docstring for StudentInfo"""
	
	def __init__(self, name, id, mark):
		self.name = name
		self.id = id
		self.mark = mark

	def talk(self):
		print(f'Hello, My name is {self.name}')
		print(f'My id is {self.id}')
		print(f'My mark is {self.mark}')

s1 = StudentInfo('sunny', 101, 90)
s2 = StudentInfo('bunny', 102, 95)
print(s2.name) # bunny
print(s1.name) # sunny