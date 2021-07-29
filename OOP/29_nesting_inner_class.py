class Outer:
    def __init__(self):
        print('outer class object')
    
    class Inner:
        def __init__(self):
            print('Inner class object')
        
        class Nested_inner:
            def __init__(self):
                print('Nested inner object')
            
            def m1(self):
                print('Nested method')

outer = Outer()
inner = outer.Inner()
nested_inner = inner.Nested_inner()
nested_inner.m1()

# ============================
class Human:
    def __init__(self, name):
        self.name = name
        self.head = self.Head()

    def info(self):
        print(f'Hello, Myself {self.name}')
        print('I am busy with ')
        self.head.talk() # Talking...
        self.head.brain.think() # Thinking...

    class Head:
        def __init__(self):
            self.brain = self.Brain()

        def talk(self):
            print('Talking....')
        
        class Brain:
            def think(self):
                print('Thinking...')

human = Human('Durga')
human.info()

# =================
# best practice
class Person:
    def __init__(self, name, date, month, year):
        self.name = name
        self.dob = self.Birth(date, month, year)

    def info(self):
        print(f'My name is {self.name}')
        self.dob.display()

    class Birth():
        def __init__(self, date, month, year):
            self.date = date
            self.month = month
            self.year = year

        def display(self):
            print(f'Birthday is {self.date}/{self.month}/{self.year}')

durga = Person('Durga', 24, 8, 1947)
durga.info()