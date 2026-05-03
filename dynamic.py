from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    def __init__(self):
        self.dim1 = 0
        self.dim2 = 0

    def setDimensions(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def showDimensions(self):
        print("First dimension :", self.dim1)
        print("Second dimension:", self.dim2)

    @abstractmethod
    def area(self):
        pass


# Rectangle class
class Rectangle(Shape):
    def area(self):
        a = self.dim1 * self.dim2
        print("Area of rectangle :", a)


# Triangle class
class Triangle(Shape):
    def area(self):
        a = self.dim1 * self.dim2 / 2
        print("Area of triangle :", a)


# Circle class
class Circle(Shape):
    def setDimensions(self, rad):
        super().setDimensions(rad, 0.0)

    def area(self):
        a = math.pi * self.dim1 * self.dim1
        print("Area of circle :", a)


# Main program
t = Triangle()
t.setDimensions(45.3, 62.4)

r = Rectangle()
r.setDimensions(76.5, 36.5)

c = Circle()
c.setDimensions(55.4)

# Dynamic Method Dispatch
ref = t
print("Triangle\n------------")
ref.showDimensions()
ref.area()

ref = r
print("\nRectangle\n------------")
ref.showDimensions()
ref.area()

ref = c
print("\nCircle\n------------")
ref.showDimensions()
ref.area()