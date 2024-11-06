from __future__ import annotations


class Product:
    """Класс продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Преобразование продукта в строку"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """Сложение двух продуктов, в результате получем общую стоимость всего имеющегося количества продуктов"""
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product: dict) -> Product:
        """Создаём новый продукт"""
        return Product(product["name"], product["description"], product["price"], product["quantity"])

    @property
    def price(self) -> float:
        """Получаем стоимость продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливаем стоимость продукта, если новая стоимость больше нуля"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
