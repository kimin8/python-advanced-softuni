class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
                self.price += price_per_quantity * quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += price_per_quantity * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient not in self.ingredients.keys():
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            else:
                if quantity > self.ingredients[ingredient]:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= price_per_quantity * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        ingredient_messages = []
        for key in self.ingredients.keys():
            ingredient_messages.append(f"{key}: {self.ingredients[key]}")
        return f"You've ordered pizza {self.name} prepared with {', '.join(ingredient_messages)} and the price will be {self.price}lv."
