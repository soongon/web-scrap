import requests
from bs4 import BeautifulSoup

# 데이터 가져오기 (HTML)
res = requests.get('https://news.naver.com/')

# soup 객체 만들기
soup = BeautifulSoup(res.text, 'html.parser')

li_list = soup.select('#today_main_news > div.hdline_news > ul > li')

headlines = []
for li in li_list:
    headlines.append(li.select_one('div:nth-child(1) > a').text.strip())

print(headlines)

# headlines 저장..
