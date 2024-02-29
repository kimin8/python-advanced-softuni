from project.product import Product


class Drink(Product):
    def __init__(self, name: str, quantity: int = 10):
        Product.__init__(self, name, quantity)
