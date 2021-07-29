# Write a Python program to implement multiple inheritance

from abc import ABC, abstractmethod

class Engine(ABC):
	@abstractmethod
	def setHorsePower(self, hrspwr): pass
	@abstractmethod
	def getHorsePower(self): pass
	@abstractmethod
	def setMaker(self, mk): pass
	@abstractmethod
	def getMaker(self): pass

class Body:
	def set_color(self, clr): self.color = clr
	def get_color(self): return self.color

class Car(Body, Engine):
	def __init__(self, hrsPwr, clr, mkr):
		self.hp = hrsPwr
		super().set_color(clr)
		self.maker = mkr

	def setHorsePower(self, hrsPwr): self.hp = hrsPwr
	def getHorsePower(self): return self.hp
	def setMaker(self, mk): self.maker = mk
	def getMaker(self): return self.maker

toyota_corolla = Car(100, 'White', 'Toyota')
pajero = Car(800, 'Black', 'Mitsubishi') 