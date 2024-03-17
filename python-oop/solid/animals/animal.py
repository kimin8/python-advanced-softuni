from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_species(self):
        pass

    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Cat(Animal):
    @staticmethod
    def make_sound() -> str:
        return "meow"

    def get_species(self) -> str:
        return self.__class__.__name__.lower()


class Dog(Animal):
    @staticmethod
    def make_sound() -> str:
        return "bark"

    def get_species(self) -> str:
        return self.__class__.__name__.lower()


class Chicken(Animal):
    @staticmethod
    def make_sound() -> str:
        return "kokokoko"

    def get_species(self) -> str:
        return self.__class__.__name__.lower()


def animal_sound(animals_list: list):
    for animal in animals_list:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
