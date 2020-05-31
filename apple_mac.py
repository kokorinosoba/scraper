#!/usr/bin/env python3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from texttable import Texttable

def get_titles_and_prices():
    url = 'https://www.apple.com/jp/shop/refurbished/mac'

    try:
        html = urlopen(url)
    except HTTPError:
        return 'URL cannot be opened', '-'

    try:
        bs = BeautifulSoup(html.read(), features='html.parser')
        #print(bs)
        prices = bs.findAll(class_='as-price-currentprice')
        titles = list(map(lambda price: price.parent.a.text.strip(), prices))
        prices = list(map(lambda price: price.text.strip(), prices))
    except AttributeError:
        return 'Attribute not found', '-'

    return titles, prices

table = Texttable()
table.add_rows([['Title', 'Price']], header=True)

titles, prices = get_titles_and_prices()

for title, price in tuple(zip(titles, prices))[:10]:
    table.add_rows([[title, price]], header=False)

print(table.draw())
