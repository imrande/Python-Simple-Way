class Student:
	def __init__(self, name, mark):
		self.name = name
		self.mark = mark

	def display(self):
		print(f'Hi, {self.name}')
		print(f'Your mark is {self.mark}')

	def grade(self):
		if self.mark >= 60:
			print('Congrats! You\'ve got first grade')
		elif self.mark >= 50:
			print('You\'ve got second grade')
		elif self.mark >= 35:
			print('You\'ve got third grade')
		else:
			print('Sorry, You are failed')
			print('Good luck for next time')

while True:
	name = input('Student name ')
	mark = int(input('Enter the mark '))
	student1 = Student(name, mark)
	student1.display()
	student1.grade()

	print('Do you want to check for another Student')
	option = input('Yes | No ').lower()
	if option == 'no':
	    print('Thank you for checking')
		break