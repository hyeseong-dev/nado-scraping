from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys 
import pyperclip

driver = webdriver.Chrome()
driver.get('https://www.naver.com')
time.sleep(1)

# 메인 화면에서 로그인 버튼 클릭
login_btn = driver.find_element_by_class_name('link_login')
login_btn.click()
time.sleep(1)

naver_id = driver.find_element_by_name('id')
naver_pw = driver.find_element_by_name('pw')

naver_id.click()
pyperclip.copy('lhs4859')
naver_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

naver_pw.click()
pyperclip.copy('password')
naver_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

login_btn = driver.find_element_by_id('log.login')
login_btn.click()

# 로그인 성공시 html 정보 출력 
print(driver.page_source)

# 브라우저 종료
driver.quit()
