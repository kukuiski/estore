from estore.product import Product


def test_product_initialization(product_samsung):
    """Тестируем начальную инициализацию продукта Samsung Galaxy S23 Ultra."""
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_product_price_setter(product_samsung, capsys):
    """Тестируем установку цены продукта с проверкой на нулевое значение."""
    # Попытка установить нулевую цену и проверка сообщения
    product_samsung.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_samsung.price == 180000.0  # Цена не должна измениться

    # Установка новой допустимой цены
    product_samsung.price = 175000.0
    assert product_samsung.price == 175000.0


def test_product_new_product():
    """Тестируем создание нового продукта из словаря с использованием метода new_product."""
    product_data = {"name": "Xiaomi Mi 11", "description": "128GB, Черный цвет", "price": 60000.0, "quantity": 10}
    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "Xiaomi Mi 11"
    assert product.description == "128GB, Черный цвет"
    assert product.price == 60000.0
    assert product.quantity == 10


def test_product_str(product_samsung):
    """Тестируем преобразование продукта в строку"""
    assert str(product_samsung) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_samsung, product_xiaomi):
    assert product_samsung + product_samsung == 1800000.0
