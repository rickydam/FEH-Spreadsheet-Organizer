import pprint

import scrape
import spreadsheet


def main():
    pp = pprint.PrettyPrinter()
    spreadsheet_object = spreadsheet.Spreadsheet("stats.json")
    scrape_object = scrape.Scrape()
    name = input("Name of hero: ").capitalize()
    heroes_data = scrape_object.scrape_hero(name)
    heroes_data = scrape_object.data_list(heroes_data, scrape_object.hero_name)
    heroes_data = scrape_object.list_into_dict(heroes_data)

    boon = input("Boon(default = neutral): ")
    bane = input("bane(default = neutral): ")
    stats = spreadsheet_object.hero_stats(heroes_data, boon, bane)
    list_stats = list(stats.values())
    list_stats.insert(0, 5)      # Hard-code rarity 5 into data
    list_stats.insert(1, scrape_object.hero_name)

    list_stats.append(boon.upper())
    list_stats.append(bane.upper())
    pp.pprint(list_stats)
    spreadsheet_object.insert_hero(list_stats)


if __name__ == '__main__':
    main()
