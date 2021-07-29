"""
Write a class definition for the following scenario -->
You have to write a class called MyFraction which works on fractions of the
form a/b where a represents the numerator and b represents the denominator. Both a and b are integers (i.e. if a = 1
and b = 2, then the fraction will be 1/2). Your class should perform the following operations:
i. Create two constructors – (1) with no parameters that set a = 0 and b = 1;
and (2) with 2 integer parameters that sets both a and b.
ii. Write an instance method for addition which returns the resultant object.
[int: a/b + c/d = (ad + bc)/bd]
iii. Write a static method for multiplication which returns the resultant object.
[Hint a/b * c/d = ac/bd]
iv. Write a main() that allocates two Fractions, 1/2 and 3/4 and stores
their sum in a third variable.
"""

class MyFraction:
	def __init__(self, a=0, b=1):
		self.a = a
		self.b = b

	def __add__(self, other):
		return MyFraction((self.a * other.b + self.b * other.a), (self.b * other.b))

	def __mul__(self, other):
		return MyFraction((self.a * other.a), (other.b * self.b))

	def __str__(self):
		return str(self.a / self.b)

if __name__ == '__main__':
	fraction1 = MyFraction(1, 2)
	fraction2 = MyFraction(3, 4)
	total_sum = fraction1 + fraction2
	total_product = fraction1 * fraction2
	print(total_product)