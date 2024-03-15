from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people  = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join([x.__repr__() for x in self.people])}"

    def __getitem__(self, idx: int) -> str:
        return f"Person {idx}: {str(self.people[idx])}"
