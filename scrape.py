import urllib.request
from bs4 import BeautifulSoup
import pprint

quote_page = 'https://feheroes.gamepedia.com/Abel'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

tables = soup.find_all('table', {'class': 'wikitable default'})
table = tables[1]
td = table.find_all('td')
for element in td:
    print(element.text)
