from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is not None:
            self.__dough = value
        else:
            raise ValueError("You should add dough to the pizza")

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        else:
            self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings.keys()) == self.__max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        else:
            if topping.topping_type in self.toppings.keys():
                self.toppings[topping.topping_type] += topping.weight
            else:
                self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self) -> int:
        total_weight = self.__dough.weight
        for topping in self.toppings.keys():
            total_weight += self.toppings[topping]

        return total_weight
