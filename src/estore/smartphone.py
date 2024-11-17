from __future__ import annotations
from estore.product import Product


class Smartphone(Product):
    """Описание класса «Смартфон»"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализация класса на основе родительского"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Smartphone) -> float:
        """
        Сложение двух продуктов типа «Смартфон», в результате получаем общую стоимость
        всего имеющегося количества смартфонов
        """
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
