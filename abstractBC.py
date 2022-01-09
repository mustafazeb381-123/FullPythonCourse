#Abstractmethd and @abstract
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    type = "Rectangle"
    side = 4
    def __init__(self):
        self.length = 6
        self.breadth = 8
    def printarea(self):
        return self.length * self.breadth
rect = Rectangle()
print(rect.printarea())