from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.__radius = radius

    def calculate_area(self) -> float:
        return self.__radius * self.__radius * pi

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height: float, width: float):
        self.__height = height
        self.__width = width

    def calculate_area(self) -> float:
        return self.__width * self.__height

    def calculate_perimeter(self) -> float:
        return 2 * self.__height + 2 * self.__width
    