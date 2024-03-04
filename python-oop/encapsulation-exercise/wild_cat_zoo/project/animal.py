class Animal:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
