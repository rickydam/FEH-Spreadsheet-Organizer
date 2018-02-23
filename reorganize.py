import pprint

import spreadsheet

pp = pprint.PrettyPrinter()
spreadsheet_object = spreadsheet.Spreadsheet("stats.json")
data = spreadsheet_object.sort_hero_data()
cell_data = []
count = 0
for hero in data:
    cell_data.append(list(hero.values()))
    count += 1
spreadsheet_object.reorganize_spreadsheet(cell_data, count)
