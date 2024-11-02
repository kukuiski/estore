# conftest.py

import pytest

from estore.category import Category
from estore.product import Product


@pytest.fixture
def product_samsung():
    """Фикстура для продукта Samsung Galaxy S23 Ultra."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category_smartphones():
    """Фикстура для категории смартфонов с двумя продуктами."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )
