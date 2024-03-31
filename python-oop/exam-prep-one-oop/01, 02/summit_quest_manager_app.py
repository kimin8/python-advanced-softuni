from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        if climber_type != "ArcticClimber" and climber_type != "SummitClimber":
            return f"{climber_type} doesn't exist in our register."

        try:
            _ = next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            self.climbers.append(ArcticClimber(climber_name)
                                 if climber_type == "ArcticClimber"
                                 else SummitClimber(climber_name))

            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        if peak_type != "ArcticPeak" and peak_type != "SummitPeak":
            return f"{peak_type} is an unknown type of peak."

        peak = ArcticPeak(peak_name, peak_elevation) \
            if peak_type == "ArcticPeak" \
            else SummitPeak(peak_name, peak_elevation)

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        missing_gear = [x for x in peak.get_recommended_gear() if x not in gear]
        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared and climber.can_climb():
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        successful_climbers = [b for b in self.climbers if len(b.conquered_peaks) > 0]
        sorted_successful_climbers = sorted(successful_climbers, key=lambda c: (-len(c.conquered_peaks), c.name))

        message = (f"Total climbed peaks: {len({p for c in successful_climbers for p in c.conquered_peaks})}\n"
                   f"**Climber's statistics:**\n")
        message += '\n'.join([str(x) for x in sorted_successful_climbers])

        return message
