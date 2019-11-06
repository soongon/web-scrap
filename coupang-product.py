import requests
from bs4 import BeautifulSoup
import pprint

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

res = requests.get(
    'https://www.coupang.com/np/campaigns/82/components/194176?page=1',
    headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

product_list = []
for li in soup.select('#productList > li'):
    product_list.append([
        li.select_one('a > dl > dd > div.name').text.strip(),
        li.select_one('a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong').text,
        li.select_one('a > dl > dd > div.other-info > div > span.rating-total-count').text
    ])

pprint.pprint(product_list)

# 김순곤