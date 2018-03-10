import pprint

import scrape
import spreadsheet


def main():
    pp = pprint.PrettyPrinter()
    spreadsheet_object = spreadsheet.Spreadsheet("stats.json")
    heroes_data = spreadsheet_object.get_heroes_stats()
    name = input("Name of hero: ")
    boon = input("Boon(default = neutral): ")
    bane = input("bane(default = neutral): ")
    stats = spreadsheet_object.hero_stats(heroes_data, name, boon, bane)
    list_stats = list(stats.values())
    list_stats.insert(0, 5)      # Hard-code rarity 5 into data
    list_stats.insert(1, name)

    list_stats.append(boon.upper())
    list_stats.append(bane.upper())
    pp.pprint(list_stats)
    spreadsheet_object.spreadsheet_work(list_stats)


if __name__ == '__main__':
    main()
