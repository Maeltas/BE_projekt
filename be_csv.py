import jsons
import pandas as pd
from dataclasses import dataclass
import json
import random
import re

categories_map = {
    "Chłodzenie": 83,
    "Zasilacze": 84,
    "Karty graficzne": 85,
    "Karty graficzne/Tesla": 94,
    "Karty graficzne/Nvidia": 95,
    "Karty graficzne/Amd": 96,
    "Pamięci": 86,
    "Akcesoria": 87,
    "Procesory": 88,
    "Procesory/Amd": 89,
    "Procesory/Intel": 90,
    "Płyty główne": 91,
    "Płyty główne/Amd": 92,
    "Płyty główne/Intel": 93,
    "Dyski": 97,
    "Dyski/Ssd": 98,
    "Dyski/Hdd": 99,
}


@dataclass
class ProductEntry:
    id: int
    category: str
    subcategory: str
    title: str
    price: float
    image: str
    link: str
    content: str

    def csv(self):
        table = []
        table.append(self.id)  # id
        table.append(1)  # active (0/1)
        table.append(self.title)
        if self.subcategory != "":
            x = str(categories_map[self.category]) + ',' + str(categories_map[self.category + '/' + self.subcategory])
            table.append(x)
        else:
            print(str(categories_map[self.category]))
            table.append(str(categories_map[self.category]))
        my_float = self.price / 1.23
        table.append(f'{my_float:.2f}')  # price tax excluded
        table.append(5)  # tax rules
        table.append(self.price)  # wholesale price
        table.append(0)  # on sale (0/1)
        table.append("")  # discount amount
        table.append("0")  # discount percent
        table.append("")  # discount from
        table.append("")  # discount to
        table.append("RP-demo_1")
        table.append("RF-demo_1")
        table.append("Hurtownia Elektronika")  # supplier
        if self.subcategory:
            if self.subcategory.lower() in ["tesla", "intel", "amd", "nvidia"]:
                table.append(self.subcategory)  # manufacturer
            else:
                table.append("")
        else:
            table.append("")
        table.append("1234567890123")  # ean13
        table.append("")  # upc
        table.append("")  # MPN
        table.append(1)  # ecotax
        table.append(0.6)  # width
        table.append(0.6)  # height
        table.append(0.6)  # depth
        table.append(0.068357)  # weight
        table.append("")  # Delivery time of in-stock products
        table.append("")  # Delivery time of out-of-stock products with allowed orders
        if self.price > 1000.0:
            table.append(random.randint(5, 20))
        else:
            table.append(random.randint(20, 100))
        table.append(1)  # minimal quantity
        table.append(5)  # low stock level
        table.append(1)  # Receive a low stock alert by email
        table.append("")  # visibility
        if self.price > 1000.0:
            table.append("")  # additional shipping cost
        else:
            table.append(10)  # additional shipping cost
        table.append("szt.")
        table.append(0)
        table.append("<p>Kolekcja klasyki, pozdrawiam i polecam, Piotr Fronczewski</p>")  # summary
        table.append(self.content)  # description
        if self.subcategory:
            table.append(self.category + "," + self.subcategory)
        else:
            table.append(self.category)
        table.append("Meta title-" + self.title.split()[0])
        table.append("Meta keywords-" + self.title.split()[0])
        table.append("Meta description-" + self.title.split()[0])
        table.append(self.link.replace(".html", ""))
        table.append("Na stanie")
        table.append("Obecnie zaopatrzenie Zamawianie jest dostępne")
        table.append(1)
        table.append("2022-12-17")
        table.append("2022-11-30")
        table.append(1)
        table.append("http://some-prestashop/img_import/" + self.link.replace("html", "jpg"))
        table.append(self.title)
        table.append(0)
        table.append("")
        table.append(1)
        table.append("new")
        table.append(0)
        table.append(0)
        table.append(0)
        table.append(0)
        table.append(0)
        table.append("")
        table.append("")
        table.append("")
        table.append("")
        table.append(0)
        table.append(0)
        table.append(0)
        table.append(0)
        # print(table)
        return table


class Category:
    def __init__(self, id, name, parent):
        self.id = id
        self.name = name
        self.parent = parent

    def csv(self):
        table = []
        table.append(self.id)  # id
        table.append(1)  # active (0/1)
        table.append(self.name)
        table.append(self.parent)
        table.append(0)  # root category (0/1)
        table.append("Opis")
        table.append("Meta title-" + self.name)
        table.append("Meta keywords-" + self.name)
        table.append("Meta description-" + self.name)
        table.append(self.name)  # URL
        table.append("")  # img url
        # print(table)
        return table


f = open("scrap.json")
data = json.loads(f.read())
products = []
categories_ids = {}
categories = []
id = 10
data.sort(key=lambda x: x["subcategory"] != "")
for product in data:
    category = product["category"].capitalize()
    subcategory = product.get("subcategory").capitalize()
    if category not in categories_ids:
        categories_ids[category] = id
        categories.append(
            Category(id, category, "Strona główna"))
        id += 1
    if subcategory != "":
        full_category = f"{category}/{subcategory}"
        if full_category not in categories_ids:
            categories_ids[full_category] = id
            categories.append(
                Category(id, subcategory, category))
            id += 1

id = 2
for product in data:
    products.append(ProductEntry(id, product["category"].capitalize(), product["subcategory"].capitalize(),
                                 product["title"].capitalize(), product["price"],
                                 product["image"], product["link"], product["content"]))
    id += 1
ct_table = []
for category in categories:
    ct_table.append(category.csv())
df = pd.DataFrame(ct_table)
df.to_csv("categories.csv", mode="w", index=False, sep=";")
pt_table = []
for product in products:
    pt_table.append(product.csv())
df = pd.DataFrame(pt_table)
df.to_csv("products.csv", mode="w", index=False, sep=";")
