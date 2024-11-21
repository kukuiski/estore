import pytest


def test_smartphone_initialization(product_smartphone_samsung):
    """Тестируем начальную инициализацию продукта Samsung Galaxy S23 Ultra."""
    assert product_smartphone_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone_samsung.price == 180000.0
    assert product_smartphone_samsung.quantity == 5
    assert product_smartphone_samsung.efficiency == 95.5
    assert product_smartphone_samsung.model == "S23 Ultra"
    assert product_smartphone_samsung.memory == 256
    assert product_smartphone_samsung.color == "Серый"


def test_smartphone_addition(product_smartphone_samsung, product_smartphone_iphone):
    """Тестируем сложение двух смартфонов."""
    assert product_smartphone_samsung + product_smartphone_iphone == 2_580_000.0


def test_smartphone_addition_typeerror(product_smartphone_samsung):
    """Тестируем исключение при сложении объектов разных типов."""
    with pytest.raises(TypeError):
        _ = product_smartphone_samsung + 1
