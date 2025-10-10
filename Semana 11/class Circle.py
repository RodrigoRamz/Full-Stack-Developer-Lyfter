
import math

class Circle: #class
    def __init__(self, radius): #constructor
        if not isinstance(radius, (int, float)): #validates the data type (variable or argument)
            raise TypeError("The radius should be a number")
        if radius <= 0:
            raise TypeError("The radius should be higher than 0")
        
        self.radius = radius #attribute


    def get_area(self): #method
        return math.pi * (self.radius ** 2)
    

c1 = Circle(1) #object (instance)
print(c1.get_area())

c2 = Circle(3)
print(c2.get_area())

c3 = Circle(10)
print(c3.get_area())