from estore.product import Product


def test_category_initialization(category_smartphones):
    """Тестируем начальную инициализацию категории и количество продуктов."""
    assert category_smartphones.name == "Смартфоны"
    assert (
        category_smartphones.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_smartphones._Category__products) == 2


def test_category_add_product(category_smartphones):
    """Тестируем добавление нового продукта в категорию."""
    new_product = Product("Xiaomi 13", "128GB, Черный цвет", 70000.0, 10)
    category_smartphones.add_product(new_product)
    assert len(category_smartphones._Category__products) == 3
    assert "Xiaomi 13, 70000.0 руб. Остаток: 10 шт." in category_smartphones.products
