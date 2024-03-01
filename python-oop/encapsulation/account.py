class Account:
    def __init__(self, id: int, balance: float, pin: int):
        self.__pin = pin
        self.__id = id
        self.balance = balance

    def get_id(self, pin: int):
        if pin == self.__pin:
            return self.__id
        else:
            return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        else:
            return "Wrong pin"
