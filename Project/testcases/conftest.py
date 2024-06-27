import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--enable-automation")
    # chrome_options.add_argument('start-maximized')
    # chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    request.cls.driver = driver  # this will make "driver" refernce availble at class level. - cls means class
    request.cls.wait = wait # this will make "wait" refernce availble at class level.
    yield
    driver.close()
    driver.quit()
