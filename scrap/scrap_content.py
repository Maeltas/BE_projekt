from dataclasses import dataclass
from typing import List

import jsons
import requests
from bs4 import BeautifulSoup

@dataclass
class ProductEntry:
    category: str
    subcategory: str
    title: str
    price: float
    image: str
    link: str

@dataclass
class Product(ProductEntry):
    content: str = ""

    @classmethod
    def from_parent(cls, p, content):
        return cls(
            p.category,
            p.subcategory,
            p.title,
            p.price,
            p.image,
            p.link,
            content
        )


def scrap_content(entry):
    r = requests.get(f"https://www.krsystem.pl/{entry.link}")
    soup = BeautifulSoup(r.text, 'html.parser')
    div = soup.find("div", {"class", "prod-clip"})
    if div is not None:
        content = div.find('table')
        return Product.from_parent(entry, str(content))
    return Product.from_parent(entry, '')

    #product = Product.from_parent(entry, content)
    #return product

if __name__ == '__main__':
    with open('scrap.json', 'r') as f:
        products = jsons.loads(f.read(), List[ProductEntry])
        products = list(map(scrap_content, products))

        with open('super_scrap.json', 'w') as w:
            w.write(jsons.dumps(products))
