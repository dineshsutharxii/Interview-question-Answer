import time

from Project_new.base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FlightSearchResultPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

        # Locator
        self.select_stops = lambda stop: (By.XPATH, "//p[normalize-space()='" + str(stop) + "']")
        self.stop = (By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")

    def filter_by_stop(self, stop):
        print(self.select_stops(stop))
        stops = self.wait.until(EC.element_to_be_clickable(self.select_stops(stop)))
        stops.click()
        time.sleep(2)

    def get_search_flight_results(self):
        search_result = self.wait.until(EC.presence_of_all_elements_located())
        return search_result

