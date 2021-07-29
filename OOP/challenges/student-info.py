"""
Design a class named Student that has two private data – student id and score. The class should contain a parameterized constructor to initialize its data member and one method to display the information. 
Now write a Python program that will use an array of Student objects to represent information about 3 students. Your program should take
input from the keyboard and display the information of the 3 students.
"""

class Student:
	def __init__(self, id, score):
		self.__id = id
		self.__score = score

	def display(self):
		print(f'ID: {self.__id}\n'
		f"Score: {self.__score}"
		)
		return None

students = []
number_of_students = int(input('Number of students '))

for i in range(number_of_students):
	id = input('Student id: ')
	score = input('Score: ')
	student = Student(id, score)
	students.append(student)

print('\nAll students info ->')
for student in students:
	student.display()