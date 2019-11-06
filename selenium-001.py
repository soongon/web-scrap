from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')

driver.implicitly_wait(3)

driver.get('https://www.melon.com/chart/index.htm')
driver.implicitly_wait(3)

html = driver.page_source
driver.close()

soup = BeautifulSoup(html, 'html.parser')

