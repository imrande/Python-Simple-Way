# we can use same operator for multiple purposes, which is called operator overloading...

class Book:
	def __init__(self, price):
		self.price = price

	def __add__(self, other):
		return self.price + other.price

crimeAndPunishment = Book(300)
theBoatManOfPadma = Book(250)
totalPrice = (crimeAndPunishment + theBoatManOfPadma)
print(f'Total price is ₹{totalPrice}')

# overloading of > and <= operators for student class objects
class Student(object):
	def __init__(self, name, mark):
		self.mark = mark
		self.name = name

	def __gt__(self, other):
		return self.mark > other.mark

	def __le__(self, other):
		return self.mark <= other.mark

student1 = Student('Ravi', 100)
student2 = Student('Durga', 200)
print(student1 > student2) # -> False
# we just only need to implement either < or > for working with both, reverse is perfectly work without implement
print(student1 < student2) # -> True
print(student1 <= student2) # -> True
print(student1 >= student2) # -> False

# program to overload * operator to work on employee objects
class Employee:
	def __init__(self, name, salaryPerDay):
		self.name = name
		self.salaryPerDay = salaryPerDay

	def __mul__(self, other):
		return self.salaryPerDay * other.workingDays

class DailySheet:
	def __init__(self, id, workingDays):
		self.id = id
		self.workingDays = workingDays

perDaySalary = Employee('Imran', 500)
numberOfDays = DailySheet('2589', 25)
# pvm is always called magic methods from first operand, otherwise it will throw Error...
monthlySalary = perDaySalary * numberOfDays
# so, order is important
# monthlySalary = numberOfDays * perDaySalary -> Error
print(f'Monthly salary is ₹{monthlySalary}')

# overloading of + operator for nesting requirements
class Bookshop:
	def __init__(self, price):
		self.price = price

	def __add__(self, other):
		return Bookshop(self.price + other.price)

	def __str__(self):
		return str(self.price)

warAndPeace = Bookshop(350)
theGambler = Bookshop(310)
theIdiot = Bookshop(270)
# + first take (war + gambler) and return bookObj, then take bookObj + idiot obj
totalPrice = warAndPeace + theGambler + theIdiot
print(type(totalPrice)) # -> <class '__main__.Bookshop'>
print(f'Total price is ₹{totalPrice}')