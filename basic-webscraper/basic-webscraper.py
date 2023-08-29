import requests
from bs4 import BeautifulSoup


URL = 'https://books.toscrape.com'

req = requests.get(URL)

# soup = BeautifulSoup(URL, 'html.parser')
# print(soup)