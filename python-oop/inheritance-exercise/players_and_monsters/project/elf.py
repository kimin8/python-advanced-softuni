from project.hero import Hero


class Elf(Hero):
    def __init__(self, username: str, level: int):
        Hero.__init__(self, username, level)
        