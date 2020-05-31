#!/usr/bin/env python3
from selenium import webdriver
from texttable import Texttable

url = 'https://www.apple.com/jp/shop/refurbished/mac'
driver = webdriver.Chrome()
driver.get(url)

titles = map(lambda e: e.text, driver.find_elements_by_class_name('as-producttile-tilelink'))
prices = map(lambda e: e.text, driver.find_elements_by_class_name('as-price-currentprice'))
# links = map(lambda e: e.get_attribute('href'), driver.find_elements_by_class_name('as-producttile-tilelink'))

table = Texttable()
table.add_rows([['Title', 'Price']], header=True)

for title, price in tuple(zip(titles, prices))[:10]:
    table.add_rows([[title, price]], header=False)

print(url)
print(table.draw())

driver.quit()
