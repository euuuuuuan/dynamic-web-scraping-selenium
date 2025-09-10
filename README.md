# 🐍 Python & Selenium: 동적 웹 스크래핑 프로젝트

---

## 🌟 프로젝트 소개
본 프로젝트는 **Python과 Selenium**을 활용하여 다양한 웹사이트에서 데이터를 수집하고, 웹 동작을 자동화하는 데 초점을 맞춘 포트폴리오입니다.  

복잡한 웹 구조와 동적인 데이터 로딩 환경에 대응하며, 실제 웹사이트 환경에서 안정적으로 작동하는 자동화 스크립트를 구현했습니다.  
또한, **AI 도구를 적극 활용**하여 문제 해결 능력과 효율적인 코드 작성 역량을 강화했습니다.

---

## 🚀 주요 기능 및 결과물

### ✅ 네이버 음악 플레이리스트 정보 수집 (`music_scroll.py`)
- **기능**:  
  웹페이지 스크롤링을 통해 모든 플레이리스트 데이터를 로딩하고,  
  제목, 해시태그, 좋아요 수, 노래 수를 수집하여 **엑셀 파일로 저장**합니다.
- **기술적 특징**:  
  - 무한 스크롤링 구현 (JavaScript 실행)  
  - 동적 콘텐츠 로딩 처리  

---

### ✅ 중앙선거관리위원회 후보자 통계 데이터 다운로드 (`poll_scraper.py`)
- **기능**:  
  중앙선거관리위원회 웹사이트에 접속하여 특정 선거(대통령 선거)의 후보자 통계(성별/연령별) 데이터를 검색하고,  
  **PDF 파일을 자동 다운로드**합니다.
- **기술적 특징**:  
  - 복잡한 메뉴/드롭다운 메뉴 선택 자동화  
  - **ActionChains**, **By.LINK_TEXT**, **WebDriverWait** 조합으로 안정성 확보  

---

### ✅ Costagram 데이터 스크래핑 (`sns_scrap.py`)
- **기능**:  
  Codeit 제공 가상 SNS 웹사이트에 로그인 → 모든 포스트 순회 →  
  이미지 주소, 제목, 좋아요, 댓글 수를 **엑셀 파일로 저장**
- **기술적 특징**:  
  - 로그인 자동화  
  - 동적 스크롤링 구현  
  - 팝업창에서 상세 정보 추출 후 메인 페이지로 복귀  

---

## 💡 기술적 성과 및 문제 해결
- **동적 웹페이지 처리**:  
  JavaScript 기반 무한 스크롤, 동적 로딩 환경을 Selenium + JS 코드 결합으로 해결
- **다양한 Selector 활용**:  
  XPath, CSS Selector, By.ID, By.CLASS_NAME 등 상황별 탐색 전략 능숙 활용
- **견고한 자동화 스크립트**:  
  `sleep()` 대신 **WebDriverWait** 사용 → 신뢰성/안정성 극대화
- **오류 처리**:  
  `try-except-finally` 구문을 통해 오류 발생 시에도 브라우저 정상 종료 보장
- **자동 드라이버 관리**:  
  **WebDriver-manager** 라이브러리를 적용하여 운영체제/Chrome 버전에 맞는 드라이버를 자동 설치 및 관리 → 프로젝트의 **휴대성과 편의성** 강화  

---

## 🤖 AI 도구 활용
본 프로젝트는 **ChatGPT, Google Gemini, Claude** 등을 활용했습니다.

- 📚 **문제 해결**: `NoSuchElementException`, `WebDriverException` 원인 분석 및 해결책 적용  
- ✨ **코드 최적화**: `sleep()` 의존성 최소화, **WebDriverWait** 기반으로 개선  
- 📝 **문서화 보조**: README 및 프로젝트 구조 정리, 실행 가이드 작성  

---

## ⚙️ 개발 환경 및 기술 스택
- ![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)  
- ![Selenium](https://img.shields.io/badge/Selenium-4.28-43B02A?style=flat-square&logo=selenium&logoColor=white)  
- ![WebDriverManager](https://img.shields.io/badge/WebDriver--manager-Automatic%20Driver%20Setup-green?style=flat-square)  
- ![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel%20Library-blue?style=flat-square)  

---

## ▶ 실행 방법

### 1️⃣ 필요한 라이브러리 설치
```
pip install selenium webdriver-manager openpyxl
```
2️⃣ 코드 실행
각 스크립트 파일은 driver_utils.py를 사용하여 드라이버를 자동으로 다운로드 및 관리합니다.
따라서 별도의 chromedriver.exe 파일이 필요하지 않습니다.

```
python music_scroll.py
python poll_scraper.py
python sns_scrap.py
```
3️⃣ GitHub Actions를 통한 자동 실행
GitHub 저장소의 .github/workflows/ 폴더에 워크플로 파일 추가

코드가 푸시될 때마다 또는 특정 시간에 자동 실행

실행 후 생성된 엑셀/PDF 파일 자동 커밋 → 저장소 최신 상태 유지
---
📂 프로젝트 구조 예시
```
web-automation-scraping/
 ┣ 📂 .github/workflows/   # GitHub Actions 워크플로 파일
 ┃ ┗ scraper.yml
 ┣ 📂 data/                # 수집한 데이터 저장 폴더 (Excel, PDF)
 ┣ 📂 screenshots/         # 실행 결과 스크린샷
 ┣ 📂 src/
 ┃ ┣ music_scroll.py        # 네이버 뮤직 플레이리스트 수집
 ┃ ┣ poll_scraper.py        # 선거 데이터 스크래핑
 ┃ ┣ sns_scrap.py           # SNS 데이터 스크래핑
 ┃ ┗ driver_utils.py        # 드라이버 관리 유틸리티
 ┣ requirements.txt         # 의존성 관리
 ┗ README.md
```
---
📸 실행 화면 예시
가상 웹페이지 스크롤링 결과

<img src="https://github.com/euuuuuuan/dynamic-web-scraping-selenium/blob/main/docs/screenshots/excel_result.png" width="500"/>


중앙선거관리위원회 PDF 다운로드 결과

<img src="https://github.com/euuuuuuan/dynamic-web-scraping-selenium/blob/main/docs/screenshots/poll_scraper_result.png" width="500"/>
---

### 🧑‍💻 개발자 정보

| 이름   | 역할               | 연락처                                                                 |
| :----- | :----------------- | :--------------------------------------------------------------------- |
| 전유안 | QA 자동화 엔지니어 | GitHub: [euuuuuuan](https://github.com/euuuuuuan)
