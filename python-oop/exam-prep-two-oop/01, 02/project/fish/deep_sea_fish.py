from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH: int = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, DeepSeaFish.TIME_TO_CATCH)

    def find_details(self):
        return (f"{self.__class__.__name__}: {self.name} [Points: "
                f"{self.points}, Time to Catch: {self.time_to_catch} seconds]")
