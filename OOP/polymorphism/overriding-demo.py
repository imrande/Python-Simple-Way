class Person:
	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

	def display(self):
		print(f'Name is {self.name}\n'
		f'Age is {self.age}\n'
		f'Height is {self.height}\n'
		f'Weight is {self.weight}'
		)

class Employee(Person):
	def __init__(self, name, age, height, weight, id, salary):
		super().__init__(name, age, height, weight)
		self.id = id
		self.salary = salary

	def display(self):
		super().display()
		print(f'Id is {self.id}\n'
		f'Salary is {self.salary}'
		)

softwareEngineer = Employee('Durga', 48, 5.5, 80, '2045', 25000)
softwareEngineer.display()