from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.naver.com')
    a_tag = driver.find_element_by_css_selector(
        '#PM_ID_serviceNavi > li:nth-child(4) > a')
    WebDriverWait(driver, 5)\
        .until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '#PM_ID_serviceNavi > li:nth-child(4) > a')))
    a_tag.click()

    b_tag = driver.find_element_by_css_selector('#lnb > div > ul > li.menu.main_isale > a')
    WebDriverWait(driver, 5) \
        .until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '#lnb > div > ul > li.menu.main_isale > a')))
    b_tag.click()

    # sendKeys('soongon')
    # click()

    time.sleep(5)
    driver.close()


main()