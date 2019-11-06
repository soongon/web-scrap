import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://www.billboard.com/charts/hot-100'

def get_html_from_url(url):
    return requests.get(url)

def main():

    res = get_html_from_url(URL)
    soup = BeautifulSoup(res.text, 'html.parser')

    billoard_top_100 = []
    for li in soup.select('#charts > div > div.chart-list.container > ol > li'):
        billoard_top_100.append([
            #li.select_one(' span.chart-element__information__song.text--truncate.color--primary').text,
            li.find('button')
                .find('span', {'class': 'chart-element__information'})
                .find('span', {'class': [
                                    'chart-element__information__song',
                                    'text--truncate',
                                    'color--primary']})
                .text,
            #li.select_one('.text--truncate.color--secondary').text
            li.find('button')
                .find('span', {'class': 'chart-element__information'})
                .find('span', {'class': [
                                        'chart-element__information__artist',
                                        'text--truncate',
                                        'color--secondary']})
                .text
        ])

    pprint.pprint(billoard_top_100)


main()