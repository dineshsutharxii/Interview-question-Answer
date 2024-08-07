import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


# from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope="class")
class ConfTest:
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=chrome_options, service=service_obj)
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        self.cls.driver = driver  # this will make "driver" refernce availble at class level. - cls means class
        self.cls.wait = wait  # this will make "wait" refernce availble at class level.
        yield
        driver.close()
        driver.quit()
