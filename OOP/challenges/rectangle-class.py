# Implement Rectangle Class Using the Encapsulation

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2

demo1 = Rectangle(4, 5)
demo1.area()
demo1.perimeter()