import pprint

import spreadsheet

pp = pprint.PrettyPrinter()
spreadsheet_object = spreadsheet.Spreadsheet("stats.json")
data = spreadsheet_object.sort_hero_data()
cell_data = []

"""
Start at y_range = 1 (and not 0) because spreadsheet row 1 is
the titles. +1 to account for this and place all hero data
below row 1.
"""
y_range = 1
for hero in data:
    cell_data.append(list(hero.values()))
    y_range += 1

spreadsheet_object.reorganize_spreadsheet(cell_data, y_range)
