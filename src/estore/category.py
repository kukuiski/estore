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

    def __str__(self):
        """Преобразование объекта в строку"""
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию c проверкой соответствия типу"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError
        return None

    def average_price(self):
        """Возвращаем среднюю стоимость продуктов или 0, если продуктов в категории нет"""
        return sum([p.price for p in self.__products]) / len(self.__products) if len(self.__products) else 0

    @property
    def products(self):
        """Получение информации о продуктах в виде строки"""
        string = ""
        for product in self.__products:
            string += f"{str(product)}\n"
        return string
