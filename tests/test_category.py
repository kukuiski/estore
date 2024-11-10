import pytest

from estore.product import Product


def test_category_initialization(category_tvs):
    """Тестируем начальную инициализацию категории и количество продуктов."""
    assert category_tvs.name == "Телевизоры"
    assert (
        category_tvs.description
        == "Телевизоры для дома с высокой четкостью изображения и умными функциями для развлечений."
    )
    assert len(category_tvs._Category__products) == 2


def test_category_add_product(category_tvs):
    """Тестируем добавление нового продукта в категорию."""
    new_product = Product("Sony Bravia XR", "75-дюймовый, 4K UHD, Full Array LED", 220000.0, 5)
    category_tvs.add_product(new_product)
    assert len(category_tvs._Category__products) == 3
    assert "Sony Bravia XR, 220000.0 руб. Остаток: 5 шт." in category_tvs.products
    with pytest.raises(TypeError):
        category_tvs.add_product("Новый продукт")


def test_category_str(category_tvs):
    """Тестируем преобразование категории в строку"""
    assert str(category_tvs) == "Телевизоры, количество продуктов: 17 шт."


def test_category_products(category_tvs):
    """Тестируем вывод списка продуктов в категории"""
    expected_output = (
        "Телевизор LG OLED55C1, 120000.0 руб. Остаток: 10 шт.\n"
        "Телевизор Samsung QN90A, 160000.0 руб. Остаток: 7 шт.\n"
    )
    assert category_tvs.products == expected_output
