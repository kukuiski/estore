from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для определения структуры класса Product"""

    @abstractmethod
    def __init__(self, *args):
        super().__init__(*args)

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass
