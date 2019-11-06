import requests
from bs4 import BeautifulSoup
import pprint

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

res = requests.get(
    'https://www.coupang.com/np/campaigns/82/components/194176',
    headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

product_list = []
for li in soup.select('#productList > li'):
    product_list.append([
        li.find('a').find('dl').find('dd')
            .find('div', {'class': 'name'})
            .text.strip(),
        li.find('a').find('dl').find('dd')
            .find('div', {'class': 'price-area'})
            .find('div', {'class': 'price-wrap'})
            .find('div', {'class': 'price'})
            .find('em').find('strong')
            .text,
        li.find('a').find('dl').find('dd')
            .find('div', {'class': 'other-info'}).find('div')
            .find('span', {'class': 'rating-total-count'})
            .text,
        'https:' + li.find('a').find('dl').find('dt').find('img')['src']
    ])

pprint.pprint(product_list)

# 김순곤