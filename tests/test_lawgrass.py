import pytest


def test_lawn_grass_initialization(product_trava_elitnaya):
    """Тестируем начальную инициализацию продукта Газонная трава Элитная."""
    assert product_trava_elitnaya.name == "Газонная трава"
    assert product_trava_elitnaya.description == "Элитная трава для газона"
    assert product_trava_elitnaya.price == 500.0
    assert product_trava_elitnaya.quantity == 20
    assert product_trava_elitnaya.country == "Россия"
    assert product_trava_elitnaya.germination_period == "7 дней"
    assert product_trava_elitnaya.color == "Зеленый"


def test_lawn_grass_addition(product_trava_elitnaya, product_trava_vinoslivaya):
    """Тестируем сложение двух видов газонной травы."""
    assert product_trava_elitnaya + product_trava_vinoslivaya == 16_750.0


def test_lawn_grass_addition_typeerror(product_trava_elitnaya):
    """Тестируем исключение при сложении объектов разных типов."""
    with pytest.raises(TypeError):
        _ = product_trava_elitnaya + 1
