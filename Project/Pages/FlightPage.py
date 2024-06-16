from selenium import webdriver
from selenium.webdriver.common.by import By
from Project.Pages.BasePage import BasePage

class FlightPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

