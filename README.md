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
- `__add__(other: Product) -> float`: Сложение двух продуктов для получения общей стоимости.
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
- `add_product(product: Product)`: Добавляет продукт в категорию и увеличивает общий счётчик продуктов.
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
