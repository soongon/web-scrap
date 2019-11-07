from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')

driver = webdriver.Chrome('./chromedriver', options=options)

driver.get('https://login.coupang.com/login/login.pang')
print('로그인 사이트 이동')
driver.get_screenshot_as_file('before-login.png')
driver.find_element_by_name('email').send_keys('soongon@gmail.com')
driver.find_element_by_name('password').send_keys(MY_PASS)
#driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[5]/button').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/form').submit()
print('로그인 수행')
time.sleep(2)
driver.get_screenshot_as_file('./login_ok.png')
print('스크린샷 완료')
driver.close()
