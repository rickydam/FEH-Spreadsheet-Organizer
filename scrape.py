import urllib.request
from bs4 import BeautifulSoup
import pprint
import json

base_url = 'https://feheroes.gamepedia.com/'
heroes_url = base_url + 'Hero_List'
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

heroes_page = urllib.request.urlopen(heroes_url)
soup = BeautifulSoup(heroes_page, 'html.parser')
table = soup.find('table')
a = table.find_all('a', title=True)
#something = a.find_all('tr')

hero_list = []
for element in a:
    hero_list.append(element['title'])

hero_list = list(filter(None, hero_list))

for element in hero_list:
    if "Story" in element:
        hero_list.remove(element)
    if "Tempest Trials" in element:
        hero_list.remove(element)
    if "Category:Legendary Heroes" in element:
        hero_list.remove(element)
    if "Category:Special Heroes" in element:
        hero_list.remove(element)
    if "Grand Hero Battle" in element:
        hero_list.remove(element)

hero_list = list(set(hero_list))
hero_list = sorted(hero_list, key=str.lower)
print(hero_list)
