# Advantages of Inheritance
    # Parent class members are by default available to child class,So we can use such members without rewrite(code reusability)
    # Child class can also define new members(code extendibility) but it is not possible to call child class members by parent class
# if u want to use parent class members with also extra members defined in child class then better use Inheritance (IS-A relationship)... [person is a employee]
# if u want to use only class members and not extending any methods better use composition(HAS-A relationship)... [employee has a car]

class P:
    def m1(self):
        print('Parent class method')

class C(P):
    def m2(self):
        print('Child class method')

c = C()
c.m2()
c.m1()

print()
# ==================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eatAndDrink(self):
        print('Eat biryani')
        print('Drink Wine')

class Employee(Person):
    def __init__(self, name, age, salary, id):
        super().__init__(name, age)
        self.salary = salary
        self.id = id

    def work(self): print('Software Engineer')
    def info(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Salary is ${self.salary}')
        print(f'Id is {self.id}')

employee = Employee('Durga', 48, 1_000_000, 87452)
employee.info()
employee.work()