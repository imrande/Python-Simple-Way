# Calculate the Student's Performance

class Student:
	def __init__(self, name, phy, chem, bio):
		self.name = name
		self.phy = phy
		self.bio = bio
		self.chem = chem

	def totalObtained(self):
		return self.phy + self.chem + self.bio

	def percentage(self):
		return (self.totalObtained() * 100) // 300

student = Student('Mark', 80, 90, 40)
print(student.totalObtained())
print(student.percentage())