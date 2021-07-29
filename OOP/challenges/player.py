"""
Implement an abstract class 'player' and two subclasses named 'batsman' and 'bowler'. Each player has a name, contact address, telephone number and status (either batsman or bowler). The batsman class maintains the total run obtained by a batsman and the number of one day matches he participated. Similarly, the bowler class maintains the total wickets taken by a player and the total number of matches. The parent class contains an abstract method to calculate the average of each player.
Implement the above classes in Python. Provide constructors to initialize the private data. Override the __str__ method in each class to display the class name. Write a program to create an object of type batsman and bowler and calculate the average run/wickets obtained by a player. Your program should also call the __str__ method to display the class name.
"""

from abc import ABC, abstractmethod

class Player(ABC):
	BATSMAN = 1
	BOWLER = 0

	def __init__(self, name, address, telephone, status):
		self._name = name
		self._address, = address,
		self._telephone = telephone
		self._status = status

	@abstractmethod
	def average(self): pass

class Batsman(Player):
	def __init__(self, name, address, telephone, status, run, matches):
		super().__init__(name, address, telephone, status)
		self.run = run
		self.matches = matches

	def __str__(self):
		return str(__class__.__name__)

	def average(self): 
		return self.run / self.matches

class Bowler(Player):
	def __init__(self, name, address, telephone, status, wicket, matches):
		super().__init__(name, address, telephone, status)
		self.wicket = wicket
		self.matches = matches
		
	def __str__(self):
		return str(__class__.__name__)

	def average(self):
		return self.wicket / self.matches

bat = Batsman('a', 'x', '10058', 'batsman', Player.BATSMAN, 18)
ball = Bowler('b', 'y', '15897', Player.BOWLER, 500, 18)

print(bat)
print(f'Average run is {bat.average():0.3f}')
print(ball)
print(f'Average wicket is {ball.average():0.3f}')
