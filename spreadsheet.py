import gspread
import json
import pprint

from collections import OrderedDict
from oauth2client.service_account import ServiceAccountCredentials


class Spreadsheet:

    def __init__(self, stats_json):
        self.stats_json = stats_json

    def get_heroes_stats(self):
        json_data = open(self.stats_json).read()
        data = json.loads(json_data, object_pairs_hook=OrderedDict)
        heroes_data = data['heroes']
        dict_data = {element['name']: element for element in heroes_data}
        return dict_data

    def spreadsheet_work(self, data):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'Fire-Emblem-Heroes-2918b0c607c7.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open(
            'Copy of Fire Emblem Heroes Bias Spreadsheet').sheet1

        pp = pprint.PrettyPrinter()
        row = data
        index = 2
        sheet.insert_row(row, index)

    def hero_stats(self, data, name, boon='neutral', bane='neutral'):
        hero = data[name]
        hero_stats = hero['stats']['40']['5']
        if boon and bane != 'neutral':
            boon_hero_stats = hero_stats[boon]
            bane_hero_stats = hero_stats[bane]

            # Change stats of Boon and Bane
            boon_stat = int(boon_hero_stats[2])
            bane_stat = int(bane_hero_stats[0])
            hero_stats[boon] = boon_stat
            hero_stats[bane] = bane_stat

        # Rest of the stats Neutral
        for k, v in hero_stats.items():
            if type(v) is list:
                hero_stats[k] = v[1]

        return hero_stats
