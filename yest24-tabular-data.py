import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.yes24.com/24/category/bestseller?CategoryNumber=001001003&sumgb=06')

soup = BeautifulSoup(res.text, 'html.parser')









