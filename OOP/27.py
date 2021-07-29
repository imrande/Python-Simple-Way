# acessing members of one class inside another class

class Employee(object):
	"""docstring for Employee"""
	def __init__(self, name, id, salary):
		self.name = name
		self.id = id
		self.salary = salary

	def display(self):
		print(f'Name is {self.name}')
		print(f'id is {self.id}')
		print(f'salary is {self.salary}')

class Manager:
	@staticmethod
	def update_salary(emp):
		emp.salary += 100_000
		emp.display()


emp = Employee('Robi', 2018, 10000)
Manager.update_salary(emp)