from selenium import webdriver

path = r"C:\Users\82109\Downloads\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://google.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("제주도")
search_box.submit()
results = driver.find_element_by_css_selector('h3>span')
for result in results:
    print(result.get_attribute("textContent"))
driver.quit()
