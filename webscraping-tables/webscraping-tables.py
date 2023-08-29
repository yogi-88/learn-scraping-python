import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_league_table(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    tablelist = []
    league_table = soup.find('table', class_='standing-table__table callfn').find('tbody')
    for team in league_table.find_all('tr'):
        pl_team = team.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        pl_points = team.find_all('td', class_='standing-table__cell')[9].text
        teaminleague = {
            'name': pl_team,
            'points': pl_points
        }
        tablelist.append(teaminleague)
    return tablelist


data = get_league_table('https://www.skysports.com/premier-league-table')
# print(data)

df = pd.DataFrame(data) # read data into dataframe
print(df.head())
df.to_csv('leaguetable.csv')
df.to_excel('leaguetable.xlsx')
print('save to file')






