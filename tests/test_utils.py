from estore.category import Category
from estore.product import Product
from estore.utils import create_objects_from_json, read_json


def test_read_json(sample_json_data):
    """Проверяем корректность чтения JSON данных из файла."""
    data = read_json(sample_json_data)
    assert isinstance(data, list)
    assert data[0]["name"] == "Телевизоры"
    assert data[0]["products"][0]["name"] == "Телевизор LG OLED55C1"


def test_create_objects_from_json(sample_json_data):
    """Проверяем создание объектов Category и Product из JSON данных."""
    data = read_json(sample_json_data)
    categories = create_objects_from_json(data)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Телевизоры"
    assert categories[0].description == "Категория телевизоров"
    assert len(categories[0]._Category__products) == 2

    product = categories[0]._Category__products[0]
    assert isinstance(product, Product)
    assert product.name == "Телевизор LG OLED55C1"
    assert product.description == "55-дюймовый 4K UHD, OLED дисплей, HDR10, AI Sound Pro"
    assert product.price == 120000.0
    assert product.quantity == 10
