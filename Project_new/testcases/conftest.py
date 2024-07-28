import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


# from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # service_obj = Service(ChromeDriverManager().install())
    service_obj = Service(r'C:\Users\dines\.wdm\drivers\chromedriver\win64\127.0.6533.72\chromedriver-win32\chromedriver.exe')

    driver = webdriver.Chrome(options=chrome_options, service=service_obj)
    wait = WebDriverWait(driver, 10)
    # driver.get("https://www.yatra.com/")
    driver.get("https://demo.softneta.com/search.html")
    driver.maximize_window()
    request.cls.driver = driver  # this will make "driver" reference available at class level. - cls means class
    request.cls.wait = wait  # this will make "wait" reference available at class level.
    yield
    driver.window_handles

    driver.close()
    driver.quit()
