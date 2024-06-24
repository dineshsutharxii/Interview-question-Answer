import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    request.cls.driver = driver  # this will make "driver" refernce availble at class level. - cls means class
    request.cls.wait = wait # this will make "wait" refernce availble at class level.
    yield
    driver.close()
    driver.quit()
