import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from Project.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightSearchPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        # locator
        # from city
        self.SEARCH_BUTTON = (By.XPATH, "//input[@value='Search Flights']")
        self.depart_city_xpath = (By.XPATH, "//label[@for='BE_flight_origin_city']")
        # self.from_city_enter_text_xpath = (By.XPATH, "//input[@placeholder='From']")
        self.city_suggestions_xpath = (By.XPATH, "//div[@class='viewport']//div[1]/li")
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
        # self.departure_date = lambda date: (By.XPATH, "//div[@aria-label='" + str(date) + "']")
        self.departure_date = (By.XPATH, "//input[@id='BE_flight_origin_date']")

    # Methods below this only
    def enter_from_location(self, from_location):
        from_loc = self.wait.until(EC.element_to_be_clickable(self.depart_city_xpath))
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
        time.sleep(2)
        click_first_suggestion = self.wait.until(EC.element_to_be_clickable(self.city_suggestions_xpath))
        click_first_suggestion.click()

    def select_date_departure(self, date):
        try:
            departure = self.wait.until(EC.visibility_of_element_located(self.date_container))
            departure.is_displayed()
        except Exception as e:
            print(f"Date container is not found : {e}")
            departure = self.wait.until(EC.visibility_of_element_located(self.departure_element))
            departure.click()
        deleteit = self.departure_date(date)
        select_date = self.wait.until(EC.visibility_of_element_located(self.departure_date(date)))
        select_date.click()

    def click_search(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        element.click()
