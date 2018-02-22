import gspread
import json
import pprint

from oauth2client.service_account import ServiceAccountCredentials

def main():
    pp = pprint.PrettyPrinter()
    heroes_data = get_heroes_stats()
    stats = hero_stats(heroes_data, 'Abel')
    pp.pprint(stats['40']['5'])

def get_heroes_stats():
    json_data = open('stats.json').read()
    data = json.loads(json_data)
    heroes_data = data['heroes']
    dict_data = {element['name']:element for element in heroes_data}
    return dict_data

def spreadsheet_work():
    scope = ['https://spreadsheets.google.com/feeds']
    #scope_string = ' '.join(scope)
    creds = ServiceAccountCredentials.from_json_keyfile_name('Fire-Emblem-Heroes-2918b0c607c7.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Copy of Fire Emblem Heroes Bias Spreadsheet').sheet1

    pp = pprint.PrettyPrinter()
    row = ["5", "Test", "1", "2", "3", "4", "5", "6", "7"]
    index = 6
    sheet.insert_row(row, index)

def hero_stats(data, name):
    hero = data[name]
    return hero['stats']

if __name__ == '__main__':
    main()
