from estore.category import Category
from estore.product import Product
from estore.utils import create_objects_from_json, read_json


def test_read_json(sample_json_data):
    """Проверяем корректность чтения JSON данных из файла."""
    data = read_json(sample_json_data)
    assert isinstance(data, list)
    assert data[0]["name"] == "Смартфоны"
    assert data[0]["products"][0]["name"] == "Samsung Galaxy S23 Ultra"


def test_create_objects_from_json(sample_json_data):
    """Проверяем создание объектов Category и Product из JSON данных."""
    data = read_json(sample_json_data)
    categories = create_objects_from_json(data)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Категория смартфонов"
    assert len(categories[0]._Category__products) == 2

    product = categories[0]._Category__products[0]
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
