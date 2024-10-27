def test_category_init(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert (
        category_smartphones.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_smartphones.products[0].name == "Samsung Galaxy S23 Ultra"
    assert category_smartphones.products[0].description == "256GB, Серый цвет, 200MP камера"
    assert category_smartphones.products[0].price == 180000.0
    assert category_smartphones.products[0].quantity == 5
    assert category_smartphones.products[1].name == "Iphone 15"
    assert category_smartphones.products[1].description == "512GB, Gray space"
    assert category_smartphones.products[1].price == 210000.0
    assert category_smartphones.products[1].quantity == 8
    assert category_smartphones.category_count == 1
    assert category_smartphones.product_count == 2
