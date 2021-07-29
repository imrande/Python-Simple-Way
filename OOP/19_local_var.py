# local variables can be used to to hold temporary results
# the local variables of a method can not be accessed from outside of that method.
# sometimes to meet temporary requirements of the programmer, we can declare variables inside a method directly without using self, className or cls. such type of variables are called local variables...

class Test:
	@staticmethod
	def average(*list1):
		return sum(list1) // len(list1) # => 25

	@staticmethod
	def wish(name='Rena'):
		for i in range(10):
			print(f'Good morning {name}')

t = Test()
print(Test.average(10,20,30,40)) # good practice call by className
print(t.average(10,20,30,40)) # bad practice
Test.wish('Reba')