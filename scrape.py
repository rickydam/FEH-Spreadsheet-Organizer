import urllib.request
from bs4 import BeautifulSoup
import pprint
import json
import re


class Scrape:

    def __init__(self):
        self.base_url = 'https://feheroes.gamepedia.com/'

    def scrape_hero(self, hero_name):
        hero_name = hero_name.replace(" ", "_").title()
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
            str(hero_name): {
                'rarity': '',
                'hp': '',
                'atk': '',
                'spd': '',
                'def': '',
                'res': '',
                'bst': ''
            }
        }

        data_index = start_index
        for k in dict_data[hero_name]:
            if k == 'name':
                pass
            else:
                dict_data[hero_name][k] = data[data_index]
                data_index += 1
        print(dict_data)

        return dict_data


    def disambiguation(self, hero_name):
        hero_name = hero_name.replace(" ", "_").title()
        hero_url = self.base_url + str(hero_name)
        page = urllib.request.urlopen(hero_url)
        soup = BeautifulSoup(page, 'html.parser')

        print(hero_url)

        if soup.find_all('div', attrs={'id': re.compile('disambig')}):
            print(f"{hero_name} has a disambiguation page, please specify "
                  f"which alternative {hero_name} you would like to choose.")

        else:
            print(f"{hero_name} does not have a disambiguation page, exiting.")
            return

        alt_hero_names = soup.find_all('a', attrs={'title': re.compile(f'^{hero_name}')})

        hero_list = []
        hero_dict = {}
        for link in alt_hero_names:
            print(link.get('title'))
            hero_list.append(link.get('title'))

        counter = 0
        for hero in hero_list:
            hero_dict[counter] = hero
            counter += 1

        choice = input(f"Choose hero from list: {hero_dict}.\n")
        try:
            choice = int(choice)
        except (ValueError, KeyError):
            print(f"{choice} was not a choice from the list.")
        alt_hero = hero_dict[choice]

        hero_url = alt_hero.replace(" ", "_").title() 
        self.scrape_hero(hero_url)

