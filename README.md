# Проект «Интернет-магазин» из блока ООП

## Описание
Создание функциональности для Интернет-магазина

## Модули

### product.py
Класс «Продукт»

#### Атрибуты

- `name` (str): Название продукта.
- `description` (str): Описание продукта.
- `price` (float): Цена продукта.
- `quantity` (int): Количество продукта на складе.
- `__price` (float, private): Приватный атрибут для хранения цены продукта.

#### Методы

- `__str__`: Возвращает строковое представление продукта.
- `__add__(other: Product) -> float`: Сложение двух продуктов для получения общей стоимости с проверкой типа.
- `new_product(cls, product: dict) -> Product`: Создаёт новый продукт из словаря.
- `price` (property): Геттер для цены продукта.
- `price.setter`: Сеттер для цены продукта, не допускающий нулевую или отрицательную стоимость.

#### Пример использования

```python
from estore.product import Product

product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
print(product.name)          # Вывод: Samsung Galaxy S23 Ultra
print(product.description)   # Вывод: 256GB, Серый цвет, 200MP камера
print(product.price)         # Вывод: 180000.0
print(product.quantity)      # Вывод: 5
```

### smartphone.py
Класс «Смартфон» — наследник класса `Product`.

#### Атрибуты
- `name` (str): Название смартфона.
- `description` (str): Описание смартфона.
- `price` (float): Цена смартфона.
- `quantity` (int): Количество смартфонов на складе.
- `efficiency` (float): Энергоэффективность смартфона.
- `model` (str): Модель смартфона.
- `memory` (int): Объем памяти устройства в ГБ.
- `color` (str): Цвет устройства.

#### Методы
- `__add__(other: Smartphone) -> float`: Сложение стоимости двух смартфонов с учетом количества.

#### Пример использования

```python
from estore.smartphone import Smartphone

# Пример создания экземпляров смартфонов
product_smartphone_samsung = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
product_smartphone_iphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

# Пример использования методов
print(product_smartphone_samsung.name)          # Вывод: Samsung Galaxy S23 Ultra
print(product_smartphone_samsung.price)         # Вывод: 180000.0
print(product_smartphone_samsung.model)         # Вывод: S23 Ultra
print(product_smartphone_samsung + product_smartphone_iphone)  # Общая стоимость всех смартфонов
```

### lawngrass.py
Класс «Трава газонная» — наследник класса `Product`.

#### Атрибуты
- `name` (str): Название травы.
- `description` (str): Описание травы.
- `price` (float): Цена травы за упаковку.
- `quantity` (int): Количество упаковок на складе.
- `country` (str): Страна происхождения травы.
- `germination_period` (str): Период прорастания в днях.
- `color` (str): Цвет травы.

#### Методы
- `__add__(other: LawnGrass) -> float`: Сложение стоимости двух видов травы с учетом количества.

#### Пример использования

```python
from estore.lawngrass import LawnGrass

# Пример создания экземпляров газонной травы
product_trava_elitnaya = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
product_trava_vinoslivaya = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

# Пример использования методов
print(product_trava_elitnaya.name)           # Вывод: Газонная трава
print(product_trava_elitnaya.price)          # Вывод: 500.0
print(product_trava_elitnaya.country)        # Вывод: Россия
print(product_trava_elitnaya + product_trava_vinoslivaya)  # Общая стоимость всех упаковок травы
```

### category.py
Класс «Категория»

#### Атрибуты

- `name` (str): Название категории.
- `description` (str): Описание категории.
- `products` (list[Product]): Список продуктов в данной категории.
- `__products` (list[Product], private): Приватный атрибут для хранения списка продуктов в категории.
- `category_count` (int): **Атрибут класса** Количество созданных категорий.
- `product_count` (int): **Атрибут класса** Количество созданных продуктов по всем категориям.

#### Методы

- `__str__`: Возвращает строковое представление категории с количеством продуктов.
- `add_product(product: Product)`: Добавляет продукт в категорию и увеличивает общий счётчик продуктов с проверкой типа.
- `products` (property): Возвращает строковое представление всех продуктов в категории.

#### Пример использования

```python
from estore.product import Product
from estore.category import Category

product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2],
    )

print(category.name)                     # Вывод: Смартфоны
print(category.description)              # Вывод: Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни
print(category.products)                 # Вывод: Строковое представление продуктов в категории
print(Category.category_count)           # Вывод: 1
print(Category.product_count)            # Вывод: 2
```

## Установка

Для установки всех зависимостей:

```bash
poetry install
```

Для активации окружения:

```bash
poetry shell
```

## Примеры данных в JSON

Примеры данных находятся в JSON: 'data/product.json'

## Использование

Запуск основного скрипта:

```bash
python main.py
```

## Тестирование

Запуск тестов:

```bash
pytest
```

Тесты покрывают ключевые функции модулей: `category.py`, `product.py`
