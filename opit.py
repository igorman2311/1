import requests
from bs4 import BeautifulSoup
import csv
URL = 'https://www.gismeteo.ru/weather-chita-4797/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 YaBrowser/20.7.1.70 Yowser/2.5 Safari/537.36',
           'accept':'*/*'}
FILE = "weater.csv"

def get_html(url, params=None) :
    r = requests.get(url, headers = HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all( class_='value')
    temp = []
    ver = ''
    for item in items:
        if item.find(class_='unit unit_temperature_c') == None :
            pass
        else:
            temp.append({
                'celsius': item.find(class_='unit unit_temperature_c').get_text()
        })
    return temp

def make_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =' ')
        #writer.writerow('Цельсий')
        for item in items:
            writer.writerow(item['celsius'])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        tempera = []
        tempera.extend(get_content(html.text))
        make_file(tempera,FILE)
    else:
        print("Error")

parse()