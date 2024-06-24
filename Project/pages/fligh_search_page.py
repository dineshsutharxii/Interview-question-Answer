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
        self.SEARCH_BUTTON = (By.XPATH, "//*[@id='top-banner']//a[contains(text(),'Search')]")
        self.from_city_xpath = (By.XPATH, "//label[@for='fromCity']")
        self.from_city_enter_text_xpath = (By.XPATH, "//input[@placeholder='From']")
        self.from_city_suggestions_xpath = (By.XPATH, "//ul[@role='listbox']/li")
        self.view_price_xpath = (By.XPATH, "//span[contains(text(),'VIEW PRICES')]")

        self.to_city_xpath = (By.XPATH, "//label[@for='toCity']")
        self.to_city_enter_text_xpath = (By.XPATH, "//input[@id='toCity']")
        self.to_city_suggestions_xpath = (By.XPATH, "//ul[@role='listbox']/li")

        self.view_price_xpath = (By.XPATH, "//span[contains(text(),'VIEW PRICES')]")

    def from_location(self, fromlocation):
        from_loc = self.wait.until(EC.element_to_be_clickable(self.from_city_xpath))
        from_loc.click()
        time.sleep(5)
        from_city_enter_text = self.wait.until(EC.visibility_of_element_located(self.from_city_enter_text_xpath))
        from_city_enter_text.send_keys(fromlocation)
        time.sleep(5)
        suggestion_list = self.driver.find_element(By.XPATH, self.from_city_suggestions_xpath)
        suggestion_list[0].click()

    def to_location(self, tolocation):
        to_loc = self.wait.until(EC.element_to_be_clickable(self.to_city_xpath))
        to_loc.click()
        to_city_enter_text = self.wait.until(EC.visibility_of_element_located(self.to_city_enter_text_xpath))
        to_city_enter_text.send_keys(tolocation)
        suggestion_list = self.driver.find_elements(By.XPATH, self.to_city_suggestions_xpath)
        suggestion_list[0].click()


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
