import pytest

from estore.product import Product


def test_product_initialization(product_tv_lg):
    """Тестируем начальную инициализацию продукта Samsung Galaxy S23 Ultra."""
    assert product_tv_lg.name == "Телевизор LG OLED55C1"
    assert product_tv_lg.description == "55-дюймовый 4K UHD, OLED дисплей, HDR10, AI Sound Pro"
    assert product_tv_lg.price == 120000.0
    assert product_tv_lg.quantity == 10


def test_product_price_setter(product_tv_lg, capsys):
    """Тестируем установку цены продукта с проверкой на нулевое значение."""
    # Попытка установить нулевую цену и проверка сообщения
    product_tv_lg.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_tv_lg.price == 120000.0  # Цена не должна измениться

    # Установка новой допустимой цены
    product_tv_lg.price = 175000.0
    assert product_tv_lg.price == 175000.0


def test_product_new_product():
    """Тестируем создание нового продукта из словаря с использованием метода new_product."""
    product_data = {
        "name": "Дрель Bosch Professional GBH 2-28 F",
        "description": "Перфоратор SDS-plus, мощность 880 Вт, 3 режима работы, корпус из металла",
        "price": 8500.0,
        "quantity": 25
    }
    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "Дрель Bosch Professional GBH 2-28 F"
    assert product.description == "Перфоратор SDS-plus, мощность 880 Вт, 3 режима работы, корпус из металла"
    assert product.price == 8500.0
    assert product.quantity == 25


def test_product_str(product_tv_lg):
    """Тестируем преобразование продукта в строку"""
    assert str(product_tv_lg) == "Телевизор LG OLED55C1, 120000.0 руб. Остаток: 10 шт."


def test_product_add(product_tv_lg, product_drill_bosh):
    """Тестируем сложение двух продуктов"""
    assert product_tv_lg + product_drill_bosh == 1_412_500.0


def test_product_add_typeerror(product_tv_lg):
    """Тестируем исключение при сложении объектов разных типов"""
    with pytest.raises(TypeError):
        result = product_tv_lg + 1
