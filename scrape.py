import urllib.request
from bs4 import BeautifulSoup
import pprint
import json
import re


class Scrape:

    def __init__(self):
        self.base_url = 'https://feheroes.gamepedia.com/'
        self.hero_name = None

    def scrape_hero(self, hero_name):
        """
        Scrape for hero's stats on feheroes wiki
        """
        self.hero_name = hero_name
        hero_dict = {}
        hero_dict = self.disambiguation()
        if hero_dict:
            choice = input(f"Choose hero from list: {hero_dict}.\n")
            try:
                choice = int(choice)
            except (ValueError, KeyError):
                print(f"{choice} was not a choice from the list.")
            self.hero_name = hero_dict[choice]

        self.hero_name = self.hero_name.replace(" ", "_").title()
        hero_url = self.base_url + str(self.hero_name)
        print(f"Web scraping {self.hero_name} at: {hero_url}")
        page = urllib.request.urlopen(hero_url)
        soup = BeautifulSoup(page, 'html.parser')

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
            str(self.hero_name): {
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
        for k in dict_data[self.hero_name]:
            if k == 'name':
                pass
            else:
                dict_data[self.hero_name][k] = data[data_index]
                data_index += 1
        print(dict_data)

        return dict_data


    def disambiguation(self):
        """
        Determine if the hero has alternative selfs from wiki's disambiguation
        page. If it does, return a dictionary of the hero's alternatives.
        """
        self.hero_name = self.hero_name.replace(" ", "_").title()
        hero_url = self.base_url + str(self.hero_name)
        page = urllib.request.urlopen(hero_url)
        soup = BeautifulSoup(page, 'html.parser')

        print(f"Web scraping {self.hero_name} at: {hero_url}")

        if soup.find_all('div', attrs={'id': re.compile('disambig')}):
            print(f"{self.hero_name} has a disambiguation page, please "
                  f"specify which alternative {self.hero_name} you would like "
                  f"to choose.")

        else:
            print(f"{self.hero_name} does not have a disambiguation page, "
                  f"exiting.")
            return

        alt_hero_names = soup.find_all(
            'a', attrs={'title': re.compile(f'^{self.hero_name}')})

        hero_list = []
        hero_dict = {}
        for link in alt_hero_names:
            print(link.get('title'))
            hero_list.append(link.get('title'))

        counter = 0
        for hero in hero_list:
            hero_dict[counter] = hero
            counter += 1

        return hero_dict

    def data_list(self, data, name):
        """
        Create a list of data elements following the FEH stat ordering
        convention and breaking the bane neutral boon stats into sub-lists
        """
        list_data = []
        list_data.append(data[name]['rarity'])
        list_data.append(data[name]['hp'])
        list_data.append(data[name]['atk'])
        list_data.append(data[name]['spd'])
        list_data.append(data[name]['def'])
        list_data.append(data[name]['res'])
        #list_data.append(data[name]['bst'])
        print(list_data)

        new_list = []
        for element in list_data:
            elem = element.split('/')
            new_list.append(elem)
        return new_list

    def list_into_dict(self, data):
        """
        Assign the list's stats back into dictionary form
        """
        dict_data = {}
        #dict_data['rarity'] = data[0]
        dict_data['hp'] = data[1]
        dict_data['atk'] = data[2]
        dict_data['spd'] = data[3]
        dict_data['def'] = data[4]
        dict_data['res'] = data[5]
        print(dict_data)
        return dict_data

