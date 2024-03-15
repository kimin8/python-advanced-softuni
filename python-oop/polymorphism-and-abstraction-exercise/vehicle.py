from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float) -> None:
        consumption_plus_conditioner = self.fuel_consumption + 0.9
        if self.fuel_quantity >= distance * consumption_plus_conditioner:
            self.fuel_quantity -= distance * consumption_plus_conditioner

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float) -> None:
        consumption_plus_conditioner = self.fuel_consumption + 1.6
        if self.fuel_quantity >= distance * consumption_plus_conditioner:
            self.fuel_quantity -= distance * consumption_plus_conditioner

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * 0.95
