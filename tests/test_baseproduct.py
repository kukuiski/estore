import pytest

from estore.baseproduct import BaseProduct
from estore.mixinlog import MixinLog


# Создаем класс для тестирования
class SomeProduct(BaseProduct, MixinLog):
    def __init__(self, name, price):
        super().__init__(name, price)
        self._name = name
        self._price = price

    def __str__(self):
        return f"{self._name}: {self._price}"

    def __add__(self, other):
        if isinstance(other, SomeProduct):
            return self.price + other.price
        raise TypeError("Сложение возможно только для объектов типа SomeProduct")

    @classmethod
    def new_product(cls, product):
        return cls(product["name"], product["price"])

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = new_price


# Тесты
def test_base_product_cannot_be_instantiated():
    # Проверяем, что невозможно создать экземпляр абстрактного класса
    with pytest.raises(TypeError):
        BaseProduct()  # Попытка создать экземпляр абстрактного класса


def test_concrete_product_initialization():
    # Проверяем инициализацию конкретного класса
    product = SomeProduct("Продукт", 100)
    assert product._name == "Продукт"
    assert product.price == 100


def test_concrete_product_str():
    # Проверяем строковое представление объекта
    product = SomeProduct("Продукт", 100)
    assert str(product) == "Продукт: 100"


def test_concrete_product_addition():
    # Проверяем сложение двух продуктов
    product1 = SomeProduct("Продукт1", 100)
    product2 = SomeProduct("Продукт2", 200)
    assert product1 + product2 == 300


def test_concrete_product_invalid_addition():
    # Проверяем ошибку при сложении с объектом другого типа
    product1 = SomeProduct("Продукт1", 100)
    with pytest.raises(TypeError):
        product1 + "Не продукт"  # Неправильный тип объекта


def test_concrete_product_new_product():
    # Проверяем создание нового продукта из словаря
    product_data = {"name": "Продукт", "price": 150}
    product = SomeProduct.new_product(product_data)
    assert product._name == "Продукт"
    assert product.price == 150


def test_concrete_product_price_setter():
    # Проверяем установку новой цены
    product = SomeProduct("Продукт", 100)
    product.price = 200
    assert product.price == 200


def test_concrete_product_negative_price():
    # Проверяем, что нельзя установить отрицательную цену
    product = SomeProduct("Продукт", 100)
    with pytest.raises(ValueError):
        product.price = -50
