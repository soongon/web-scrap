from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    driver = webdriver.Chrome('./chromedriver', options=options)
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

    driver.get_screenshot_as_file('test.png')
    driver.close()


main()