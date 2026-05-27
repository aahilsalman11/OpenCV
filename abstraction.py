from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.142 * self.radius

circle1 = Circle(5)
print(circle1.area())
print(circle1.perimeter())


