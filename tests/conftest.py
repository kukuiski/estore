import json

import pytest

from estore.category import Category
from estore.lawngrass import LawnGrass
from estore.product import Product
from estore.smartphone import Smartphone


@pytest.fixture
def product_tv_lg():
    """Фикстура для продукта Samsung Galaxy S23 Ultra."""
    return Product("Телевизор LG OLED55C1", "55-дюймовый 4K UHD, OLED дисплей, HDR10, AI Sound Pro", 120000.0, 10)


@pytest.fixture
def product_drill_bosh():
    """Фикстура для продукта Xiaomi"""
    return Product(
        "Дрель Bosch Professional GBH 2-28 F",
        "Перфоратор SDS-plus, мощность 880 Вт, 3 режима работы, корпус из металла",
        8500.0,
        25,
    )


@pytest.fixture
def product_trava_elitnaya():
    """Фикстура для продукта «Газонная трава Элитная»"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_trava_vinoslivaya():
    """Фикстура для продукта «Газонная трава Выносливая»"""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def product_smartphone_samsung():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_smartphone_iphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def category_tvs():
    """Фикстура для категории телевизоров с двумя продуктами."""
    return Category(
        "Телевизоры",
        "Телевизоры для дома с высокой четкостью изображения и умными функциями для развлечений.",
        [
            Product("Телевизор LG OLED55C1", "55-дюймовый 4K UHD, OLED дисплей, HDR10, AI Sound Pro", 120000.0, 10),
            Product("Телевизор Samsung QN90A", "65-дюймовый Neo QLED, 4K UHD, Quantum HDR 32X", 160000.0, 7),
        ],
    )


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category("Пустая категория", "Категория без продуктов", [])


@pytest.fixture
def sample_json_data(tmp_path):
    """Создает временный JSON-файл с тестовыми данными и возвращает путь к нему."""
    data = [
        {
            "name": "Телевизоры",
            "description": "Категория телевизоров",
            "products": [
                {
                    "name": "Телевизор LG OLED55C1",
                    "description": "55-дюймовый 4K UHD, OLED дисплей, HDR10, AI Sound Pro",
                    "price": 120000.0,
                    "quantity": 10,
                },
                {
                    "name": "Телевизор Samsung QN90A",
                    "description": "65-дюймовый Neo QLED, 4K UHD, Quantum HDR 32X",
                    "price": 160000.0,
                    "quantity": 7,
                },
            ],
        }
    ]
    json_file = tmp_path / "products.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    return str(json_file)
