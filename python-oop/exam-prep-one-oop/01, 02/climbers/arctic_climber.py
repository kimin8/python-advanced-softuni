from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH: float = 200

    def __init__(self, name: str):
        super().__init__(name, ArcticClimber.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= 100

    def climb(self, peak: BasePeak) -> None:
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)


