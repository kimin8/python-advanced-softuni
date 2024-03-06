class Shop:


    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def add_item(self, item_name: str) -> str:
        if item_name in self.items.keys():
            current_quantity = self.items[item_name]
            if current_quantity < self.capacity:
                self.items[item_name] += 1
                return f"{item_name} added to the shop"
            else:
                return "Not enough capacity in the shop"
        else:
            self.items[item_name] = 1
            return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name in self.items.keys() and self.items[item_name] - amount >= 0:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
