from project.animal import Animal


class Cat(Animal):
    def __repr__(self) -> str:
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    @staticmethod
    def make_sound() -> str:
        return "Meow meow!"
