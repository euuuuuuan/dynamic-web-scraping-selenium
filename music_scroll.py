from time import sleep
from openpyxl import Workbook
from selenium import webdriver
from driver_utils import get_chrome_driver
from selenium.webdriver.common.by import By

wb = Workbook(write_only=True)
ws = wb.create_sheet('플레이리스트')
ws.append(['제목', '해시태그', '좋아요 수', '노래 수'])

driver = get_chrome_driver()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
sleep(3)

# 현재 scrollHeight 가져오기
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    # scrollHeight까지 스크롤
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 새로운 내용 로딩될 때까지 기다림
    sleep(1)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
    
# 스크롤 완료

playlists = driver.find_elements(by=By.CSS_SELECTOR, value='div.playlist__meta')

for playlist in playlists:
    title = playlist.find_element(by=By.CSS_SELECTOR, value='h3.title').text
    hashtags = playlist.find_element(by=By.CSS_SELECTOR, value='p.tags').text
    like_count = playlist.find_element(by=By.CSS_SELECTOR, value='span.data__like-count').text
    music_count = playlist.find_element(by=By.CSS_SELECTOR, value='span.data__music-count').text
    ws.append([title, hashtags, like_count, music_count])

driver.quit()

wb.save('플레이리스트.xlsx')