import re

import requests
from bs4 import BeautifulSoup


URL = 'https://books.toscrape.com'
req = requests.get(URL)
# print(req.status_code) to check if it is working
soup = BeautifulSoup(req.content, 'html.parser')

articles = soup.find_all('article', class_='product_pod')

book_list = []
# print(articles)
for book in articles:
    # print(book)
    title = book.find('h3').text
    # print(title)
    price = book.find('p',class_='price_color').text
    # print(price)
    instock = book.find('p',class_='instock availability').text.strip()
    # print(instock)
    books = {
        'Title': title,
        'Price': price,
        'InStock': instock
    }
    book_list.append(books)




print(book_list)