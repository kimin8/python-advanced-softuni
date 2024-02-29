from project.hero import Hero


class Knight(Hero):
    def __init__(self, username: str, level: int):
        Hero.__init__(self, username, level)
