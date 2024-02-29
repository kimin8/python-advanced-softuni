from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str:
        try:
            target = next(filter(lambda t: t.name == product_name, self.products))
            return target
        except StopIteration:
            return "Product not found."

    def remove(self, product_name: str):
        try:
            target = next(filter(lambda t: t.name == product_name, self.products))
            self.products.remove(target)
        except StopIteration:
            return "Product not found."

    def __repr__(self):
        message = ""
        for product in self.products:
            message += f"{product.name}: {product.quantity}\n"
        return message.strip()
