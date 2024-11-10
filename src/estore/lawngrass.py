from __future__ import annotations
from estore.product import Product


class LawnGrass(Product):
    """Описание класса «Трава газонная»"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализация класса на основе родительского"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: LawnGrass) -> float:
        """
        Сложение двух продуктов типа «Трава газонная», в результате получаем общую стоимость
        всего имеющегося количества травы
        """
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
