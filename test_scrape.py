import scrape


def main():
    scrape_object = scrape.Scrape()
    hero_name = input("Name of hero: ")
    scrape_object.scrape_hero(hero_name)

    #scrape_object.scrape_hero('Abel')
    #scrape_object.scrape_hero('Lyn (Love Abounds)')
    #scrape_object.scrape_hero('lyn (love abounds)')
    #scrape_object.scrape_hero('Xander')
    #scrape_object.disambiguation('Xander')
    #scrape_object.disambiguation('Abel')

if __name__ == '__main__':
    main()
