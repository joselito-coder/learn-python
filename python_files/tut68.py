from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea():
        return 0

class Rectangle(Shape):
    shape = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printArea(self):
        return  self.length * self.breadth

class Square(Shape):
    shape = "Square"
    sides = 4

    def __init__(self):
        self.length = 69

    def printArea(self):
        return self.length ** 2





rect1 = Rectangle()

print(rect1.printArea())

sq = Square()
print(sq.printArea())