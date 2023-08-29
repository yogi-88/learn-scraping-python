import requests
from bs4 import BeautifulSoup

URL = 'https://www.skysports.com/premier-league-table'

req = requests.get(URL)

# print(req.status_code)

soup = BeautifulSoup(req.content, 'html.parser')

league_table = soup.find('table',class_='standing-table__table callfn').find('tbody')

# print(league_table)

for row in league_table.find_all('tr'):
    pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
    # print(pl_team)
    pl_points = row.find_all('td', class_='standing-table__cell')[9].text
    print(pl_team, pl_points)





