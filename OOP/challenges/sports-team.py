# Aggregation practice

"""
You have to implement 3 classes: School, Team, and Player, such that an instance of a School should contain instances of Team objects. Similarly, a Team object can contain instances of Player class.

You have to implement a School class containing a list of Team objects, and a Team class comprising of a list of Player objects.
"""

class Player:
	def __init__(self, ID, name, teamName):
		self.ID = ID
		self.name = name
		self.teamName = teamName

class Team:
	def __init__(self, name):
		self.name = name
		self.players = []

	def addPlayer(self, player):
		self.players.append(player)

	def getNumberOfPlayers(self):
		return len(self.players)

class School:
	def __init__(self, name):
		self.teams = []
		self.name = name

	def addTeam(self, team):
		self.teams.append(team)

	def getTotalPlayersInSchool(self):
		length = 0
		for player in self.teams:
			length += (player.getNumberOfPlayers())
		return length

p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)

blue_team = Team("Blue Team")
blue_team.addPlayer(p2)
blue_team.addPlayer(p3)

mySchool = School("My School")
mySchool.addTeam(red_team)
mySchool.addTeam(blue_team)

print("Total players in mySchool:", mySchool.getTotalPlayersInSchool())