import pytest
import selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Basepage:
    @pytest.fixture(scope='function')
    def driver(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield self.driver
        self.driver.close()
        self.driver.quit()
