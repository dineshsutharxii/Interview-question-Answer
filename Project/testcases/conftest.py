import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.makemytrip.com/")