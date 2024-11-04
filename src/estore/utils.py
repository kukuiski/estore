import json
from pathlib import Path

from estore.category import Category
from estore.product import Product


def read_json(path: str) -> dict:
    json_path = Path(path)
    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)
    return data


def create_objects_from_json(data: dict):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


# if __name__ == "__main__":
#     file_data = read_json("../../data/products.json")
#     categories_list = create_objects_from_json(file_data)
#     for c in categories_list:
#         print(c.name)
#         print(c.description)
#         for p in c.products:
#             print(p.name)
#             print(p.description)
#             print(p.price)
#             print(p.quantity)
#     print(Category.category_count)
#     print(Category.product_count)
