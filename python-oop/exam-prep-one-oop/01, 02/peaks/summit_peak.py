from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    RECOMMENDED_GEAR: list = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self) -> list:
        return SummitPeak.RECOMMENDED_GEAR

    def calculate_difficulty_level(self) -> str:
        if self.elevation > 2500:
            return "Extreme"
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"
