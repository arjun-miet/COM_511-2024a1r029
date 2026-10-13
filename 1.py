""" Create a rectangle class with length and breadth . Use inheritance mehtods to calculate its area and perimeter."""

class Rectangle:
    def __init__(self,length , breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        print("Perimeter of rectangle:" , 2*(self.length + self.breadth))

    def area(self):
        print("Area of rectangle:" , self.length * self.breadth)

rect = Rectangle(10,10)
rect.perimeter()
rect.area()