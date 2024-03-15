from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250_000
    sponsors = {
        "Oracle": {
            1: 1_500_000,
            2: 800_000
        },
        "Honda": {
            8: 20_000,
            10: 10_000
        }
    }

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        total = 0

        for sponsor_dict in RedBullTeam.sponsors.values():
            for pos in sponsor_dict:
                if race_pos <= pos:
                    total += sponsor_dict[pos]
                    break

        total -= RedBullTeam.EXPENSES_PER_RACE

        self.budget += total
        return f"The revenue after the race is {total}$. Current budget {self.budget}$"
