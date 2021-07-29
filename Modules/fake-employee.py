import random
import string

alphabets = string.ascii_letters
digits = string.digits
cities = ['Dhaka', 'Khulna', 'Rangpur', 'Barisal', 'Mymensingh', 'Comilla']
designation = ['Software Engineer', 'Project Manager', 'Team lead', 'Project lead']

# Name Generator
def get_name():
	""" name range 3 to 10 and first char should be upper """
	name = ''
	name_range = random.randint(3, 10)

	for i in range(name_range):
		name += random.choice(alphabets)

	return name.capitalize()

# Id Generator
def get_id():
	"""
	start with 'e-' followed by 4 digit numbers
	return e-[4digit]
	"""
	id = 'e-'
	for i in range(1, 5):
		id += random.choice(digits)

	return id

# Salary Generator
def get_salary():
	""" salary range between 10000 to 50000 """
	salary = f'{random.uniform(10000, 50000):.3f}'
	return salary

# City Generator
def get_city():
	""" Generating the city between cities """
	return random.choice(cities)

# Status
def get_designation():
	""" Generating fake employee designation """
	return random.choice(designation)

# Number Generator
def get_number():
	""" Generating phone number """
	phnNumber = '+8801'
	phnNumber += str(random.randint(3, 9))

	for i in range(8):
		phnNumber += random.choice(digits)

	return phnNumber


print('Details of Employee :-')
print(get_name())
print(get_id())
print(get_salary())
print(get_city())
print(get_designation())
print(get_number())