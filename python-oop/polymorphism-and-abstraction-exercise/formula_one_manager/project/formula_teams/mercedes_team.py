from project.formula_teams.formula_team import FormulaTeam


# noinspection SpellCheckingInspection
class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200_000
    sponsors = {
        "Petronas": {
            1: 1_000_000,
            3: 500_000
        },
        "TeamViewer": {
            5: 100_000,
            7: 50_000
        }
    }

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        total = 0

        for sponsor_dict in MercedesTeam.sponsors.values():
            for pos in sponsor_dict:
                if race_pos <= pos:
                    total += sponsor_dict[pos]
                    break

        total -= MercedesTeam.EXPENSES_PER_RACE

        self.budget += total
        return f"The revenue after the race is {total}$. Current budget {self.budget}$"
