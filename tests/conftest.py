import json

import pytest

from estore.category import Category
from estore.product import Product


@pytest.fixture
def product_samsung():
    """Фикстура для продукта Samsung Galaxy S23 Ultra."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_xiaomi():
    """Фикстура для продукта Xiaomi"""
    return Product("Xiaomi Mi 11", "128GB, Черный цвет", 60000.0, 10)


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


@pytest.fixture
def sample_json_data(tmp_path):
    """Создает временный JSON-файл с тестовыми данными и возвращает путь к нему."""
    data = [
        {
            "name": "Смартфоны",
            "description": "Категория смартфонов",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            ],
        }
    ]
    json_file = tmp_path / "products.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    return str(json_file)
