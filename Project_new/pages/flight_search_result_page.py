from Project_new.base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FlightSearchResultPage(BasePage):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        # Locator
        self.select_stops = lambda stop: (By.XPATH, "//p[normalize-space()='" + stop + "']")

    def select_stop(self, stop):
        stops = self.wait.until(EC.element_to_be_clickable(self.select_stops(stop)))
        stops.click()
