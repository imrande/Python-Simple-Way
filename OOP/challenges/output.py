# Consider the following Python code & generate the output

class Owl:
	def __init__(self, string, num):
		self.string = string
		self.num = num

	def __add__(self, other):
		return self.string + " " + str(other.num)

ob = Owl('Hello', 123)
ob1 = Owl('World', 345)
new_str = ob + ob1
print(new_str) # Hello 345