
import math

class Circle: #class
    def __init__(self, radius): #constructor
        self.radius = radius #attribute


    def get_area(self): #method
        return math.pi * (self.radius ** 2)
    

c1 = Circle(1) #object (instance)
print(c1.get_area())

c2 = Circle(3)
print(c2.get_area())

c3 = Circle(10)
print(c3.get_area())