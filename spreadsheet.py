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

        row = data
        index = 2
        sheet.insert_row(row, index)

    def reorganize_spreadsheet(self, data, y_range):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'Fire-Emblem-Heroes-2918b0c607c7.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open(
            'Copy of Fire Emblem Heroes Bias Spreadsheet')
        worksheet = sheet.get_worksheet(0)
        cell_list = worksheet.range('A' + str(2) + ':' + 'I' + str(y_range))

        data_count = 0
        cell_count = 0
        for cell in cell_list:
            cell.value = data[data_count][cell_count]
            if cell_count > 7:
                data_count += 1
                cell_count = 0
            else:
                cell_count += 1

        worksheet.update_cells(cell_list)

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

    def sort_hero_data(self):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'Fire-Emblem-Heroes-2918b0c607c7.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open(
            'Copy of Fire Emblem Heroes Bias Spreadsheet')
        worksheet = sheet.get_worksheet(0)

        records = worksheet.get_all_records()
        new_record = sorted(records, key=lambda k: k["Heroes"])
        return new_record
