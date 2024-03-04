from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float) -> str:
        if self.__budget >= price and self.__animal_capacity - len(self.animals) > 0:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity - len(self.animals) > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity - len(self.workers) > 0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        try:
            worker = next(filter(lambda n: n.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care

        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: str) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        animals_status_report = f"You have {len(self.animals)} animals"

        lions = list(filter(lambda current: current.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda current: current.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda current: current.__class__.__name__ == "Cheetah", self.animals))

        animals_status_report += f"\n----- {len(lions)} Lions:"
        for lion in lions:
            animals_status_report += f"\n{lion.__repr__()}"

        animals_status_report += f"\n----- {len(tigers)} Tigers:"
        for tiger in tigers:
            animals_status_report += f"\n{tiger.__repr__()}"

        animals_status_report += f"\n----- {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            animals_status_report += f"\n{cheetah.__repr__()}"

        return animals_status_report

    def workers_status(self) -> str:
        workers_status_report = f"You have {len(self.workers)} workers"

        keepers = list(filter(lambda current: current.__class__.__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda current: current.__class__.__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda current: current.__class__.__name__ == "Vet", self.workers))

        workers_status_report += f"\n----- {len(keepers)} Keepers:"
        for keeper in keepers:
            workers_status_report += f"\n{keeper.__repr__()}"

        workers_status_report += f"\n----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            workers_status_report += f"\n{caretaker.__repr__()}"

        workers_status_report += f"\n----- {len(vets)} Vets:"
        for vet in vets:
            workers_status_report += f"\n{vet.__repr__()}"

        return workers_status_report
