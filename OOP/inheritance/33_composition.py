# How to use member of one class inside another class
# 2 way we can fulfill our requirement
# By HAS-A relationship(composition)
    # compose bigger object with some small small objects
# By IS-A relationship(Inheritance)
# look at composition and aggregation notes in note section (difference between)

# Composition example
class Engine:
    def m1(self):
        print('Engine specific functionality')

class Car2:
    def __init__(self):
        self.engine = Engine() # without car engine is not exist, they are strongly associated
    
    def m2(self):
        print('Car required engine functionality')
        self.engine.m1()

car2 = Car2()
car2.m2()

# Aggregation example
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def get_info(self):
        print(f"""Car name {self.name}
Car model {self.model}
Car color {self.color}""")

class Employee:
    def __init__(self, name, id, car):
        self.car = car
        self.name = name
        self.id = id

    def emp_info(self):
        print(f"""Employee name {self.name}
Employee id {self.id}
Employee car :-""")
        self.car.get_info()

car = Car('Innova','2.5v' ,'Grey') # without employee car object maybe exist,they are not strongly associated
emp = Employee('durga', 872425, car)
emp.emp_info()

print()
# ==============
class SportsNews:
    def sports_info(self):
        print('Sports Information 1')
        print('Sports Information 2')
        print('Sports Information 3')

class MovieNews:
    def cinema_info(self):
        print('Cinema information 1')
        print('Cinema information 2')
        print('Cinema information 3')

class PoliticsNews():
    def political_info(self):
        print('political information 1')
        print('political information 2')
        print('political information 3')

class DurgaNews:
    def __init__(self):
        self.sports = SportsNews()
        self.cinema = MovieNews()
        self.politocal = PoliticsNews()

    def full_news(self):
        print('Welcome to DurgaNews:-')
        print('Sports news are :-')
        self.sports.sports_info()

        print('Cinema news are :-')
        self.cinema.cinema_info()

        print('politocal news are :-')
        self.politocal.political_info()

newsChannel = DurgaNews()
newsChannel.full_news()