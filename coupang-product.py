import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import time

BASE_URL = 'https://www.coupang.com/np/campaigns/82/components/194176'
HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

def get_html_with_page(p_num):
    time.sleep(1)
    print('scrap ' + str(p_num) + 'page')
    return requests.get(BASE_URL + '?page=' + str(p_num), headers=HEADERS)

def no_product(soup):
    if not soup.find(id='productList'):
        print('product no more find.. Im out')
        return True

def main():
    product_list = []
    for page_num in range(1, 100):
        res = get_html_with_page(page_num)
        soup = BeautifulSoup(res.text, 'html.parser')

        if no_product(soup):
            break

        for li in soup.select('#productList > li'):
            product = [
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
            ]
            print(product)
            product_list.append(product)
            download_and_save_image('https:' + li.find('a').find('dl').find('dt').find('img')['src'])

    pprint.pprint(product_list)
    print(len(product_list))

    save_product_list(product_list)

def save_product_list(list):
    df = pd.DataFrame(list,
                      columns=['상품명','가격','좋아요','URL'])
    df.to_excel('coupang.xlsx')
    df.to_csv('coupang.csv')
    print('save to excel.. good job..')


def download_and_save_image(image_url):
    res = requests.get(image_url)
    file_name = './images/' + image_url.split('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(res.content)

main()
