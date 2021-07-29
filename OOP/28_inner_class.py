# The class which is declared inside another class

# when should use inner class
# without existing one type of object(outer class), if there is not chance of existing another type of object(inner class)

class University:
    class department:
        pass

# Advantages of inner class
# improves security, improves modularity...

class Outer:
    def __init__(self):
        print('Outer class object')
        # self.inner = self.Inner()
    
    class Inner:
        def __init__(self):
            print('Inner class object')
        
        def m1(self):
            print('Inner class Method')

# one way
outer = Outer()
inner = outer.Inner()
inner.m1()

# 2nd way
# outer = Outer()
# outer.inner.m1()
# uncomment self.inner