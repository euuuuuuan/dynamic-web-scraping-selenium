from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 드라이버 생성
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # 선거 웹사이트 접속
    driver.get('http://info.nec.go.kr/main/main_load.xhtml')

    # '후보자' 메뉴에 마우스 호버 (3초 대기)
    gnb_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "후보자")))
    ActionChains(driver).move_to_element(gnb_menu).perform()
    sleep(3) # 하위 메뉴가 나타날 시간을 줍니다.

    # '후보자 통계' 링크 클릭 (3초 대기)
    candidate_stats_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "후보자 통계")))
    candidate_stats_link.click()
    sleep(3) # 페이지가 전환될 시간을 줍니다.

    # '성별/연령별' 탭 클릭 (3초 대기)
    gender_age_tab = wait.until(EC.element_to_be_clickable((By.ID, 'searchType4')))
    gender_age_tab.click()
    sleep(3)

    # '대통령 선거' 드롭다운 메뉴 선택 (3초 대기)
    election_select = Select(wait.until(EC.element_to_be_clickable((By.ID, 'electionCode'))))
    election_select.select_by_visible_text('대통령선거')
    sleep(3)

    # '남' 드롭다운 메뉴 선택 (3초 대기)
    gender_select = Select(wait.until(EC.element_to_be_clickable((By.ID, 'genderCode'))))
    gender_select.select_by_visible_text('남')
    sleep(3)

    # '검색' 버튼 클릭 (3초 대기)
    search_button = wait.until(EC.element_to_be_clickable((By.ID, 'spanSubmit')))
    search_button.click()
    sleep(3)

    # PDF 다운로드 버튼 클릭
    pdf_download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentarea"]/div[2]/div[2]/div[1]/div/a[1]')))
    pdf_download_button.click()
    sleep(10) # 다운로드가 완료될 시간을 충분히 줍니다.

    print("✔️ '후보자 통계' 데이터 다운로드가 완료되었습니다.")

except Exception as e:
    print(f"⚠️ 오류가 발생했습니다: {e}")

finally:
    driver.quit()