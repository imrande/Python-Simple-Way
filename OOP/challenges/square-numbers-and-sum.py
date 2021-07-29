# Square Numbers and Return Their Sum

class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def sqSum(self):
		return sum(i*i for i in [self.x, self.y, self.z])

point = Point(1, 3, 5)
print(point.sqSum())