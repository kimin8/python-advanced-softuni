from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    RECOMMENDED_GEAR: list = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self) -> list:
        return ArcticPeak.RECOMMENDED_GEAR

    def calculate_difficulty_level(self) -> str:
        if self.elevation > 3000:
            return "Extreme"
        elif 2000 <= self.elevation <= 3000:
            return "Advanced"
