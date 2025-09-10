from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_chrome_driver(download_dir=None):
    """
    Chrome WebDriver 인스턴스를 생성하여 반환합니다.
    download_dir 인자를 통해 다운로드 경로를 설정할 수 있습니다.
    """
    options = Options()
    if download_dir:
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        })
    
    # 수정된 부분: 옵션만 인자로 전달하고, 드라이버 경로는 webdriver-manager가 자동으로 처리합니다.
    driver = webdriver.Chrome(options=options)
    
    return driver