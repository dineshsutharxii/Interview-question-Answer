from selenium import webdriver
from selenium.webdriver.common.by import By
from Project.Pages.BasePage import BasePage


class FlightPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # locator
    SEARCH_BUTTON_xpath = "//*[@id='top-banner']//a[contains(text(),'Search')]"
    from_city_xpath = "//label[@for='fromCity']"
    from_city_enter_text_xpath = "//input[@id='fromCity']"
    from_city_suggestions_xpath = "//ul[@role='listbox']/li"

    def Click_Search(self):
        self.driver.find_element(By.XPATH, self.SEARCH_BUTTON_xpath).click()

    def Click_From(self):
        self.driver.find_element(By.XPATH, self.from_city_xpath).click()

    def Enter_From_City(self, city="Mumbai"):
        self.driver.find_element(By.XPATH, self.from_city_enter_text_xpath).send_keys(city)

