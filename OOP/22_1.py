class Student:
	def set_name(self, name): self.name = name
	def set_mark(self, mark):self.mark = mark

	def get_name(self): return self.name
	def get_mark(self): return self.mark

n = int(input('Enter no of Students '))
Students = []

for i in range(n):
	s = Student()
	name = input('Enter name ')
	mark = int(input('Enter mark '))
	s.set_name(name)
	s.set_mark(mark)

	Students.append(s)

for s in Students:
	print(f'Hello, {s.get_name()}')
	print(f'Mark is, {s.get_mark()}')
	print()