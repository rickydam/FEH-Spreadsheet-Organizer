import scrape


def main():
    scrape_object = scrape.Scrape()
    scrape_object.scrape_hero('Abel')
    scrape_object.scrape_hero('Lyn (Love Abounds)')
    scrape_object.scrape_hero('lyn (love abounds)')
    scrape_object.scrape_hero('Xander')

if __name__ == '__main__':
    main()
