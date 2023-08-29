import requests
from bs4 import BeautifulSoup

URL = 'https://www.skysports.com/premier-league-table'

req = requests.get(URL)

# print(req.status_code)

soup = BeautifulSoup(req.content, 'html.parser')

league_table = soup.find_all('table')

for table in league_table:
    city = table.find_all('a')
    print(city.get_text())


