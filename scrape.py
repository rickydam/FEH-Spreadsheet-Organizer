import urllib.request
from bs4 import BeautifulSoup
import pprint
import json

quote_page = 'https://feheroes.gamepedia.com/Abel'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

tables = soup.find_all('table', {'class': 'wikitable default'})
table = tables[1]
td = table.find_all('td')

data = []
for stat in td:
    data.append(stat.text)

dict_data = {
    'rarity': data[7],
    'hp': data[8],
    'atk': data[9],
    'spd': data[10],
    'def': data[11],
    'res': data[12]
}

print(dict_data)
