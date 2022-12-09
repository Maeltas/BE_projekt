import jsons

from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class ProductEntry:
    category: str
    subcategory: str
    title: str
    price: float
    image: str
    link: str

def to_price(string):
    string = string
    for x in ['\n', '\t', '<', '>', '/', 'small', ' ']:
        string = string.replace(x, '')
    return float(string.replace(',', '.').split('z')[0])

def to_image_src(string):
    return string.split('\'', 1)[1].split('&', 1)[0]

def to_product(soup, category, subcategory):
    src_div = soup.find("div", {"class", "prodimg"})
    image = to_image_src(src_div['style'])
    title = soup.find("div", {"class": "col-sm-8"}).h2.string
    # - W MAGAZYNIE!!!
    title = title.replace("W MAGAZYNIE", '').replace("NA MAGAZYNIE", '').strip(" \t\n\b-!")
    price = to_price(soup.find("div", {"class": "cena"}).text)
    link = src_div.a["href"].replace("https://www.krsystem.pl/", '')
    return ProductEntry(category, subcategory, title, price, image, link)

def wierd_name(name):
    return len(name) > 120 or any(x in name for x in ['\'', '\"', '\\', '/', '>'])

def get_products(file, category, subcategory=''):
    with open(file, 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        return list(
            filter(lambda x: x.price > 0 and (not wierd_name(x.title)),
                   map(lambda x: to_product(x, category, subcategory),
                       soup.find_all("div", {"class", "product-med"})
                   )
            )
        )

def disk_select(product):
    title = product.title.lower()
    if any(x in title for x in ["ssd", "m.2", "pcie", "nvme"]):
        product.subcategory = "ssd"
    else:
        product.subcategory = "hdd"
    return product

def gpu_select(product):
    title = product.title.lower()
    if any(x in title for x in ["amd", "radeon"]):
        product.subcategory = "AMD"
        return product
    if "intel" in title:
        product.subcategory = "Intel"
        return product
    if "tesla" in title:
        product.subcategory = "Tesla"
        return product
    if any(x in title for x in ["nvidia", "geforce", "rtx", "quadro"]):
        product.subcategory = "Nvidia"
        return product
    return product

if __name__ == '__main__':
    products = []
    products.extend(get_products('html/KR System - Procesory AMD.html', "procesory", "AMD"))
    products.extend(get_products('html/KR System - Procesory Intel.html', "procesory", "Intel"))
    products.extend(get_products('html/KR System - Plyty Glowne AMD.html', "płyty główne", "AMD"))
    products.extend(get_products('html/KR System - Plyty Glowne Intel.html', "płyty główne", "Intel"))
    products.extend(get_products('html/KR System - Chlodzenie CPU.html', "chłodzenie"))
    products.extend(get_products('html/KR System - Zasilacze.html', "zasilacze"))
    products.extend(map(gpu_select, get_products('html/KR System - Karty Graficzne.html', "karty graficzne")))
    products.extend(get_products('html/KR System - Pamieci.html', "pamięci"))
    products.extend(get_products('html/KR System - Podzespoly _ akcesoria.html', "akcesoria"))
    products.extend(map(disk_select, get_products('html/KR System - HDD _ SSD.html', "dyski")))
    
    print(len(products))
    with open("scrap.json", 'w') as f:
        f.write(jsons.dumps(products))

