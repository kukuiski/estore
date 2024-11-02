def test_product_initialization(product_samsung):
    """Тестируем начальную инициализацию продукта Samsung Galaxy S23 Ultra."""
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_product_price_setter(product_samsung):
    """Тестируем установку цены продукта с проверкой на отрицательное значение."""
    product_samsung.price = -5000.0  # Попытка установить отрицательную цену
    assert product_samsung.price == 180000.0  # Цена не должна измениться
    product_samsung.price = 175000.0  # Устанавливаем новую допустимую цену
    assert product_samsung.price == 175000.0
