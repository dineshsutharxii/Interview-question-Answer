import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from Project.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import selenium


class FlightSearchPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        # locator
        # from city
        self.SEARCH_BUTTON = (By.XPATH, "//*[@id='top-banner']//a[contains(text(),'Search')]")
        self.from_city_xpath = (By.XPATH, "//label[@for='fromCity']")
        self.from_city_enter_text_xpath = (By.XPATH, "//input[@placeholder='From']")
        self.city_suggestions_xpath = (By.XPATH, "//ul[@role='listbox']/li")
        self.view_price_xpath = (By.XPATH, "//span[contains(text(),'VIEW PRICES')]")

        # to city
        self.to_city_xpath = (By.XPATH, "//label[@for='toCity']")
        self.to_city_enter_text_xpath = (By.XPATH, "//input[@placeholder='To']")

        # departure element
        self.departure_element = (By.XPATH, "//label[@for='departure']")

        # return element
        self.return_element = (By.XPATH, "//label[@for='return']")

        # date container
        self.date_container = (By.XPATH, "//div[@class='datePickerContainer']")

        # search button
        self.view_price_xpath = (By.XPATH, "//span[contains(text(),'VIEW PRICES')]")

        # departure date
        self.departure_date = lambda date: (By.XPATH, "//div[@aria-label='" + str(date) + "']")

    # Methods below this only
    def enter_from_location(self, from_location):
        from_loc = self.wait.until(EC.element_to_be_clickable(self.from_city_xpath))
        from_loc.click()
        from_city_enter_text = self.wait.until(EC.visibility_of_element_located(self.from_city_enter_text_xpath))
        from_city_enter_text.send_keys(from_location)
        click_first_suggestion = self.wait.until(EC.element_to_be_clickable(self.city_suggestions_xpath))
        click_first_suggestion.click()

    def enter_to_location(self, to_location):
        to_loc = self.wait.until(EC.element_to_be_clickable(self.to_city_xpath))
        to_loc.click()
        to_city_enter_text = self.wait.until(EC.visibility_of_element_located(self.to_city_enter_text_xpath))
        to_city_enter_text.send_keys(to_location)
        click_first_suggestion = self.wait.until(EC.element_to_be_clickable(self.city_suggestions_xpath))
        click_first_suggestion.click()

    def select_date_departure(self, date):
        try:
            self.driver.find_element(self.date_container)
        except Exception as e:
            print(f"Date container is not found : {e}")
            self.driver.find_element(self.departure_element).click()
        select_date = self.driver.find_element(self.departure_date(date))
        select_date.click()

    def Click_Search(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
            element.click()
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
