from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH: int = 90

    def __init__(self, name: str, points: float):
        super().__init__(name, points, PredatoryFish.TIME_TO_CATCH)

    def find_details(self) -> str:
        return (f"{self.__class__.__name__}: {self.name} [Points: "
                f"{self.points}, Time to Catch: {self.time_to_catch} seconds]")
