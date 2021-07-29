# You have to implement a Sedan class, which inherits from the Car class and contains a SedanEngine object.

# Composition practice
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def printDetails(self):
        print(f'Model: {self.model}')
        print(f'Color: {self.color}')
        
class SedanEngine:
    def start(self):
        print('Car has started.')
        
    def stop(self):
        print('Car has stopped.')
        
class Sedan(Car):
    def __init__(self, model, color):
        super().__init__(model, color)
        self.sedan_engine = SedanEngine()
    
    def setStart(self):
        self.sedan_engine.start()
    
    def setStop(self):
        self.sedan_engine.stop()

car1 = Sedan('Toyota', 'Grey')
car1.setStart()
car1.printDetails()
car1.setStop()
