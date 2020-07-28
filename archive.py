import requests
from bs4 import BeautifulSoup
URL = 'https://www.gismeteo.ru/weather-chita-4797/'
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 YaBrowser/20.7.1.70 Yowser/2.5 Safari/537.36',
           'accept':'*/*'}

def get_html(url, params=None) :
    r = requests.get(url, headers = HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all( class_='value')
    temp = []
    ver = ''
    for item in items:
        temp.append({
            'celsius' : item.find(class_='unit unit_temperature_c')

        })



    temp.pop()
    temp.pop()
    temp.pop()
    temp.pop()
    temp.pop()
    temp.pop()
    temp.pop()
    temp.pop()
    print(temp[1].get_text())

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")

parse()