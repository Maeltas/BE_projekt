from dataclasses import dataclass
from typing import List

import jsons
import requests

@dataclass
class ProductEntry:
    category: str
    subcategory: str
    title: str
    price: float
    image: str
    link: str

def save_image(product):
    with open(f"../prestashop/img/{product.link.replace('.html', '.jpg')}", 'wb') as f:
        r = requests.get(f"https://www.krsystem.pl/{product.image}", stream=True)
        for chunk in r:
            f.write(chunk)

if __name__ == '__main__':
    with open('scrap.json', 'r') as f:
        products = jsons.loads(f.read(), List[ProductEntry])
        for product in products:
            save_image(product)

