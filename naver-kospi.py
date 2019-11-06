import requests
from bs4 import BeautifulSoup

# 1. https://finance.naver.com/sise/ 에서 HTML 파일을 받아옴
# requests 모듈을 사용..

res = requests.get('https://finance.naver.com/sise/')
html_from_server = res.text

# 2. 받아온 HTML 파일에서 코스피지수를 포함하는 <span> 태그를 찾는다
# 3. 찾아서 데이터를 확보한다. (2130.3)
# 특정 태그를 찾는 기술
#  1. css selector
#  2. XPath 문법
#  3. 정규식을 활용 방식

# HTML Parsing.. BeautifulSoup
# 1. parsable HTML 생성
# 2. 파싱 도구 제공..
soup = BeautifulSoup(html_from_server, 'html.parser')

the_tag = soup.select_one('#contentarea > div.box_top_submain2 > div.lft > ul > li:nth-child(1) > a > span.blind')
print(the_tag.text)


# 4. 데이터를 저장한다.





#KOSPI_now

#contentarea > div.box_top_submain2 > div.lft > ul > li:nth-child(1) > a > span.blind

#//*[@id="contentarea"]/div[1]/div[1]/ul/li[1]/a/span[1]

#today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a