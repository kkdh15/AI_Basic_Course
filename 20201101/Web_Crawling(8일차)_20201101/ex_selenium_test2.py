import time
from selenium import webdriver

path = r"C:\python_lecture\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys("강릉")
search_box.submit()
time.sleep(5)
results = driver.find_elements_by_css_selector('h3>span')

for result in results:
    print(result.get_attribute("textContent"))

#first_result = driver.find_element_by_css_selector('h3>span')
#print(first_result.get_attribute("textContent")) 
time.sleep(5)
driver.quit()