import re

import requests
from bs4 import BeautifulSoup


URL = 'https://books.toscrape.com'
req = requests.get(URL)
# print(req.status_code) to check if it is working
soup = BeautifulSoup(req.content, 'html.parser')

articles = soup.find_all('article', class_='product_pod')

# print(articles)
for book in articles:
    print(book)
    title = book.find('h3').text
    print(title)
    price = book.find('p',class_='price_color').text
    print(price)
    stock_availability = book.find('p',class_='instock availability').text
    print(stock_availability)

