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
