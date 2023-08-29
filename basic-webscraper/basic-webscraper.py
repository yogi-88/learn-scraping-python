
import sys
import requests
from bs4 import BeautifulSoup
book_list = []

for i in range(1,51):
    print(i)
    URL = f'https://books.toscrape.com/catalogue/page-{i}.html'
    req = requests.get(URL)
    # print(req.status_code) to check if it is working
    soup = BeautifulSoup(req.content, 'html.parser')

    articles = soup.find_all('article', class_='product_pod')


    # print(articles)
    for book in articles:
        # print(book)
        title = book.find_all('a')[1]['title']
        # print(title)
        price = book.find('p', class_='price_color').text
        # print(price)
        instock = book.find('p', class_='instock availability').text.strip()
        # print(instock)
        books = {
            'Title': title,
            'Price': price,
            'InStock': instock
        }
        book_list.append(books)

print(len(book_list))



