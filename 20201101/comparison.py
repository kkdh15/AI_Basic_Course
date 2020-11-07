# 1. google.com -> 검색창 ->인터파크 투어 -> 검색 -> 1첫번째 사이트 이동
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup as bs
import time
from Tour_Info import TourInfo

path = r"C:\Users\82109\Downloads\chromedriver.exe"

search_keyword_interpark = "인터파크 투어"
search_keyword_jaju = "제주도"
tour_list = []

with wd.Chrome(path) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "q").send_keys(
        search_keyword_interpark + Keys.RETURN)
    #결과값 대기 나오면 실행
    first_result = wait.until(
        presence_of_element_located((By.CSS_SELECTOR, "h3>span")))

    print(first_result.get_attribute("textContent"))
    first_result.click()
    # Implicit Waits 최대 10초
    driver.implicitly_wait(10)

    # 2. 인터파크 사이트 : 검색창 -> 제주도 -> 국내여행 -> 107개를 확인
    driver.find_element_by_id('box').send_keys(search_keyword_jaju)
    driver.find_element_by_css_selector('.search-btn').click()  # 제주도 찾기
    driver.implicitly_wait(10)
    driver.find_element_by_id('li_T').click()  # 국내여행
    time.sleep(5)

# 3. 11페이지를 넘기며 -> 전체 제목을 출력
# searchModule.SetCategoryList(2, '')
    for page in range(1, 2):  # page
        driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
        time.sleep(3)
        print("%s 페이지 이동" % page)
        boxItems = driver.find_elements_by_css_selector(".dTravelBox>.boxList>.boxItem")

        for li in boxItems[1:]:  # 10개 여행업체
            title = li.find_element_by_css_selector("h5.proTit").text
            price = li.find_element_by_css_selector(".proPrice").text
            link_url = li.find_element_by_css_selector("a").get_attribute(
                'onclick').lstrip("searchModule.OnClickDetail(").rstrip(",'')")
            link_url = link_url.lstrip("'")
            info_list = li.find_elements_by_css_selector(".info-row .proInfo")[:-1]
            period = info_list[0].text
            start_time = info_list[1].text
            score = info_list[2].text

            #print(title, price, link_url, period, start_time, score, sep="\n", end='\n')            
            #print("="*100)
            obj= TourInfo(title, price, link_url, period, start_time, score)
            tour_list.append(obj)        

    #print(tour_list, len(tour_list))

    for tour in tour_list:
        driver.get(tour.link)
        time.sleep(2)
        soup = bs(driver.page_source, 'html.parser')
        tatle = soup.find('h2',{'class' : 'default-section goods-info'})
        print(tatle)