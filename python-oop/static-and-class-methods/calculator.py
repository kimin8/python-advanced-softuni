from functools import reduce


class Calculator:
    @staticmethod
    def add(*args) -> float:
        return sum(args)

    @staticmethod
    def multiply(*args) -> float:
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args) -> float:
        return reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args) -> float:
        return reduce(lambda a, b: a - b, args)
