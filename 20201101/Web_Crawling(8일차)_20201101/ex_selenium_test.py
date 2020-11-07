#https://www.selenium.dev/documentation/ko/
#인스톨은 필수! $ pip install selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time # time lib는 새로 추가

#This example requires Selenium WebDriver 3.13 or newer
# chromedriver.exe 파일이 다른곳에 있으면 새롭게 지정
#path = "C:\python_lecture\chromedriver.exe"
#with webdriver.Chrome(path) as driver:

# 브라우저에 따라 변경
# api 참조 => https://selenium-python.readthedocs.io/api.html
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    time.sleep(5)
    driver.find_element(By.NAME, "q").send_keys("제주도" + Keys.RETURN)
    time.sleep(5)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>span")))
    time.sleep(5)
    print(first_result.get_attribute("textContent"))  