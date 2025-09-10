from time import sleep
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver_utils.py에서 드라이버 생성 함수 import
from driver_utils import get_chrome_driver

# 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "Costagram Data"
ws.append(['이미지 주소', '제목', '해시태그', '좋아요 수', '댓글 수'])

# 웹 드라이버 설정
# get_chrome_driver() 함수를 사용하여 드라이버를 가져옵니다.
driver = get_chrome_driver()
driver.maximize_window()
driver.implicitly_wait(5)

try:
    driver.get('https://workey.codeit.kr/costagram/index')
    sleep(1)

    # 로그인
    driver.find_element(by=By.CSS_SELECTOR, value='.top-nav__login-link').click()
    sleep(1)

    driver.find_element(by=By.CSS_SELECTOR, value='.login-container__login-input').send_keys('codeit')
    driver.find_element(by=By.CSS_SELECTOR, value='.login-container__password-input').send_keys('datascience')
    driver.find_element(by=By.CSS_SELECTOR, value='.login-container__login-button').click()
    sleep(1)

    # 페이지 끝까지 스크롤
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 중복 방지를 위한 추적 리스트
    visited_posts = set()

    # 모든 썸네일 요소 가져오기
    posts = driver.find_elements(by=By.CSS_SELECTOR, value='.post-list__post')
    print(f"총 {len(posts)}개의 포스트를 발견했습니다.")

    for i in range(len(posts)):
        posts = driver.find_elements(by=By.CSS_SELECTOR, value='.post-list__post')
        if i < len(posts):
            post = posts[i]
            try:
                post.click()

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.post-container__image'))
                )
                style_attr = driver.find_element(by=By.CSS_SELECTOR, value='.post-container__image').get_attribute('style')
                image_path = style_attr.split('"')[1]
                image_url = 'https://workey.codeit.kr' + image_path

                content = driver.find_element(by=By.CSS_SELECTOR, value='.content__text').text.strip()
                hashtags = driver.find_element(by=By.CSS_SELECTOR, value='.content__tag-cover').text.strip()
                like_count = driver.find_element(by=By.CSS_SELECTOR, value='.content__like-count').text.strip()
                comment_count = driver.find_element(by=By.CSS_SELECTOR, value='.content__comment-count').text.strip()

                ws.append([image_url, content, hashtags, like_count, comment_count])

                driver.find_element(by=By.CSS_SELECTOR, value='.close-btn').click()
                sleep(0.5)

            except Exception as e:
                print(f"포스트 처리 중 오류 발생: {e}")
                try:
                    driver.find_element(by=By.CSS_SELECTOR, value='.close-btn').click()
                except Exception:
                    pass

finally:
    # 브라우저 종료
    driver.quit()

    # 엑셀 저장
    wb.save('코스타그램.xlsx')
    print("엑셀 파일이 저장되었습니다.")