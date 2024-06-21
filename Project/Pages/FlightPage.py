from selenium import webdriver
from selenium.webdriver.common.by import By
from Project.Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # locator
    SEARCH_BUTTON = (By.XPATH, "//*[@id='top-banner']//a[contains(text(),'Search')]")
    from_city_xpath = (By.XPATH, "//label[@for='fromCity']")
    from_city_enter_text_xpath = (By.XPATH, "//input[@id='fromCity']")
    from_city_suggestions_xpath = (By.XPATH, "//ul[@role='listbox']/li")
    view_price_xpath = (By.XPATH, "//span[contains(text(),'VIEW PRICES')]")

    def Click_Search(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
            self.driver.find_element(self.SEARCH_BUTTON).click()
        except Exception as e:
            print("The error is : ", e)

    def Click_From(self):
        self.driver.find_element(By.XPATH, self.from_city_xpath).click()

    def Enter_From_City(self, city="Mumbai"):
        self.driver.find_element(By.XPATH, self.from_city_enter_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.from_city_enter_text_xpath).send_keys(city)

    def Select_city_from_suggestion_list(self):
        suggestion_list = self.driver.find_elements(By.XPATH, self.from_city_suggestions_xpath)
        suggestion_list[0].click()
