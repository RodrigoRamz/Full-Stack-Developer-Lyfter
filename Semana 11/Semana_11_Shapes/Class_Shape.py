from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        "Abstract Method: Print the shape perimeter"
        pass

    @abstractmethod
    def calculate_area(self):
        """Abstract Method: Print the shape area"""
        pass