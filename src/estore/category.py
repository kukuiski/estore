from estore.product import Product


class Category:
    """Класс категории продуктов"""

    name: str
    description: str
    __products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        return

    @property
    def products(self):
        string = ""
        for product in self.__products:
            string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return string
