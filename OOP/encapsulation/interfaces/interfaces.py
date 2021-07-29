# python doesn't provide anything for support interfaces...
# Difference between abstract class and interface class
	# abstract class can contain abstract method and non abstract method
	# interface class only contain abstract method

from abc import ABC, abstractmethod
class CollegeAutomation(ABC):
	@abstractmethod
	def getStudentAttdence(self): pass

	@abstractmethod
	def updateStudentAttdence(self): pass

	@abstractmethod
	def getMarks(self): pass

	@abstractmethod
	def getFeeInfo(self): pass

	@abstractmethod
	def updateFee(self): pass

class DurgaSoft(CollegeAutomation):
	def getStudentAttdence(self): return 'student Sheet'

	def updateStudentAttdence(self): return 'Monthly Sheet'

	def getMarks(self): return 'Subject Marks'

	def getFeeInfo(self): return 'Payment fees'

	def updateFee(self): return 'Full Payment details'