import urllib.request
from bs4 import BeautifulSoup
import pprint
import json
import re


class Scrape:

    def __init__(self):
        self.base_url = 'https://feheroes.gamepedia.com/'

    def scrape_hero(self, hero_name):
        hero_url = self.base_url + str(hero_name)
        page = urllib.request.urlopen(hero_url)
        soup = BeautifulSoup(page, 'html.parser')

        print(hero_url)

        tables = soup.find_all('table', {'class': 'wikitable default'})
        table = tables[1]
        td = table.find_all('td')
        data = []

        for stat in td:
            data.append(stat.text)
        print(data)

        start_index = 0
        for stat in data:
            if stat == '5':
                break
            start_index += 1

        dict_data = {
            'name': str(hero_name),
            'rarity': '',
            'hp': '',
            'atk': '',
            'spd': '',
            'def': '',
            'res': '',
            'bst': ''
        }

        data_index = start_index
        for k in dict_data:
            if k == 'name':
                pass
            else:
                dict_data[k] = data[data_index]
                data_index += 1

        print(dict_data)
