# What is abstract class?
	# Abstract class is not fully implemented class, Partially implemented class
# What is abstract methods?
	# Abstract method, which has only declaration but not implementation...
# Advantages of abstract methods?
	# by declaring abstract methods in parent class we can provide guideline to child classes which methods they should be compulsory implement...
# Who is responsible to provide implementation abstract methods?
	# child class are responsible to provide full implementation...

from abc import ABC, abstractmethod
class Vehicle(ABC):
	@abstractmethod
	def getNoOfVehicles(self):
		pass

class Bus(Vehicle):
	def getNoOfVehicles(self):
		print(f'Number of Vehicle is 6')

class Auto(Vehicle):
	def getNoOfVehicles(self):
		print(f'Number of Vehicle is 3')

VillageLine = Bus()
VillageLine.getNoOfVehicles()

CnG = Auto()
CnG.getNoOfVehicles()