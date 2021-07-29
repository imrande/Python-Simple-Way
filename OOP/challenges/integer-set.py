"""
Create a class named IntegerSet. This class should contain two sets of integer
numbers that belong to the range 0 to 100. Each set is represented using an array of boolean. Array element a[i] is true if integer i is in the set. 

Your class should perform the following operations:
i. Create a no-argument constructor to initialize both of the set as anempty
set (all the elements are set to false).
ii. Create a constructor to take input into both of the sets.
iii. Write a method unionOfSets to create a third set which is the union of the
existing two sets. (An element of the third set is true if that element is true in either or both of the existing sets).
iv. Write a static method insertElement to insert a new integer k into the first
set (by setting a[k] to true).
v. Write a method printSet to print the elements of both the sets.
Write a Python program to create an object of type IntegerSet and perform all the operations mentioned in the class on that object. 
"""

class IntegerSet:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def union_of_sets(self):
		c = [False] * 20
		for i in range(20):
			if self.a[i] == True or self.b[i] == True:
				c[i] = True
		return c

	def insert_element(self, value):
		self.a[value] = True

	def print_set(self):
		print(self.a)
		print(self.b)

set_1 = list((False for i in range(0, 20)))
set_2 = list((False for i in range(0, 20)))
integer_set = IntegerSet(set_1, set_2)
integer_set.insert_element(5)
integer_set.insert_element(15)
z = integer_set.union_of_sets()
print(z)
print()
print(integer_set.print_set())