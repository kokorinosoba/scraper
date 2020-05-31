#!/usr/bin/env python3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from texttable import Texttable

def get_title_and_price(product_id):
    url = f'https://www.amazon.co.jp/dp/{product_id}'

    try:
        html = urlopen(url)
    except HTTPError:
        return 'URL cannot be opened', '-'

    try:
        bs = BeautifulSoup(html.read(), features='html.parser')
        title = bs.find(id='productTitle').get_text().strip()
        price = bs.find(id='price_inside_buybox').get_text().strip()
    except AttributeError:
        return 'Attribute not found', '-'

    return title, price

product_ids = [
    'B00MIBN71I',
    'B01GCJP1XS',
]

table = Texttable()
table.add_rows([['ID', 'Title', 'Price']], header=True)

for product_id in product_ids:
    table.add_rows([[product_id, *get_title_and_price(product_id)]], header=False)

print(table.draw())