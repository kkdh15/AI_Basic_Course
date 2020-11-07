# https://www.seoul.go.kr/coronaV/coronaStatus.do#status_page_top

# 서울에서 발생한 코로나 환자에 대한 테이블 모두
# Web Crawling -> .txt 저장

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

search_keyword_seoul_corona = "코로나19 서울 현황"
patient_list = []

path = r"C:\Users\82109\Downloads\chromedriver.exe"

with wd.Chrome(path) as driver:
    wait = WebDriverWait(driver, 2)
    driver.get("https://google.com")
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "q").send_keys(
        search_keyword_seoul_corona + Keys.RETURN)

    first_result = wait.until(
        presence_of_element_located((By.CSS_SELECTOR, "h3>span")))

    print(first_result.get_attribute("textContent"))
    first_result.click()
 
    driver.implicitly_wait(5)


    # 2. table 을 가져와서 header 를 뽑아낸다

    # 파일 작성 시작 (MS오피스에서 한글이 정상적으로 열리도록 'utf-8-sig' encoding 사용)
    with open('D:/Seoul-covid.csv','w', encoding='utf-8-sig') as file_obj:

        # 환자 내용이 들어있는 table 가져오기
        table = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]')
        # table 에서 header 가져오기
        heads = table.find_elements_by_xpath("thead/tr/th")
        colCount = len(heads)
        print(colCount)
        headStr = ''
        for h in heads:
            headStr += h.text + ','
        headStrF = headStr[:-1]
        # header 출력 및 파일에 쓰기
        print(headStrF)
        file_obj.write(headStrF + '\n')

        # 환자 내용 가져오기
        nextBtnCount = 1

        # 마지막 페이지 까지 while 로 반복 작업
        while nextBtnCount > 0:
            nextBtns = driver.find_elements_by_xpath('//*[@class="paginate_button next"]')
            nextBtnCount = len(nextBtns)
            print(nextBtnCount)
            rowCount = len(table.find_elements_by_xpath("tbody/tr"))
            print(rowCount)

            for i in range(1, rowCount+1):
                piStr = ''
                # iterate over columns
                for j in range(1, colCount+1) :
                    # get text from the i th row and j th column
                    if j == 1:
                        piStr += table.find_element_by_xpath("tbody/tr["+str(i)+"]/th").text + ','
                    else:
                        piStr += table.find_element_by_xpath("tbody/tr["+str(i)+"]/td["+str(j-1)+"]").text + ','

                piStrF = piStr[:-1]
                print(piStrF)
                file_obj.writelines(piStrF + '\n')

            if nextBtnCount > 0:
                nextBtns[0].click()
            driver.implicitly_wait(5)


        print("--- program write end ---")

