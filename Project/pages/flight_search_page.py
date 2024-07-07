import time

from selenium import webdriver
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from Project.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightSearchPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        # locator
        # from city
        self.depart_city_xpath = (By.XPATH, "//input[@id='BE_flight_origin_city']")
        self.select_city_from_suggestion = (By.XPATH, "//div[@class ='viewport']//li[1]")

        # to city
        self.to_city_xpath = (By.XPATH, "//input[@id='BE_flight_arrival_city']")

        # departure element
        self.departure_element = (By.XPATH, "//input[@id='BE_flight_origin_date']")

        # return element
        self.return_element = (By.XPATH, "//input[@id='BE_flight_arrival_date']")

        # search button
        self.SEARCH_BUTTON = (By.XPATH, "//*[@id='BE_flight_flsearch_btn']")
        # self.view_price_xpath = (By.XPATH, "//span[contains(text(),'VIEW PRICES')]")

        # departure date
        # self.departure_date = lambda date: (By.XPATH, "//div[@aria-label='" + str(date) + "']")
        self.departure_date = (By.XPATH, "//input[@id='BE_flight_origin_date']")
        self.select_departure_date = lambda date: (By.XPATH, "//*[@id='" + date + "']")

    # Methods below this only
    def enter_from_location(self, from_location):
        from_loc = self.wait.until(EC.element_to_be_clickable(self.depart_city_xpath))
        from_loc.click()
        from_loc = self.wait.until(EC.element_to_be_clickable(self.depart_city_xpath))
        from_loc.send_keys(from_location)
        select_depart_loc = self.wait.until(EC.element_to_be_clickable(self.select_city_from_suggestion))
        select_depart_loc.click()

    def enter_to_location(self, to_location):
        to_loc = self.wait.until(EC.element_to_be_clickable(self.to_city_xpath))
        to_loc.click()
        to_loc.send_keys(to_location)
        select_depart_loc = self.wait.until(EC.element_to_be_clickable(self.select_city_from_suggestion))
        select_depart_loc.click()

    def select_date_departure(self, date):
        try:
            departure = self.wait.until(EC.visibility_of_element_located(self.departure_date))
            departure.is_displayed()
        except Exception as e:
            print(f"Date container is not found : {e}")
            departure = self.wait.until(EC.visibility_of_element_located(self.departure_element))
        departure.click()
        print(self.select_departure_date(date))
        select_date = self.wait.until(EC.visibility_of_element_located(self.select_departure_date(date)))
        select_date.click()

    def click_search(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        element.click()
