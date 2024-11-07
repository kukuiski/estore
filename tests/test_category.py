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


def test_category_str(category_smartphones):
    """Тестируем преобразование категории в строку"""
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 13 шт."


def test_category_products(category_smartphones):
    """Тестируем вывод списка продуктов в категории"""
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category_smartphones.products == expected_output
