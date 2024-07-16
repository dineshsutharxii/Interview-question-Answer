import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Project_new.pages.flight_search_page import FlightSearchPage


@pytest.mark.usefixtures("setup")
class TestSearchFlightAndVerifyResults:
    def test_search_flight(self):
        fs = FlightSearchPage(self.driver, self.wait)
        fs.enter_from_location("BOM")
        fs.enter_to_location("Bangalore")
        fs.select_date_departure("17/08/2024")
        fs.click_search()
        time.sleep(2)

#
# # Setup
# @pytest.(scope='function')
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get('https://www.goibibo.com/flights/')
#     yield driver
#     driver.close()
#     driver.quit()
#
#
# # Function to wait for an element to be present
#
#
# class Test_Flight:
#
#     # testcases Case 1.1: Verify that the page loads successfully
#     def test_page_loads(self, driver):
#         assert "Goibibo" in driver.title
#         print("Page loaded successfully")
#
#     # testcases Case 2.1: Verify that the "One-way" radio button is selected by default
#     def test_one_way_selected(self, driver):
#         one_way_radio = driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div/div/div[1]/ul/li[1]/span")
#         assert one_way_radio.is_selected(), "One-way radio button is not selected by default"
#         print("One-way radio button is selected by default")
#
#     # testcases Case 2.2: Verify the functionality of the "Round-trip" radio button
#     def test_round_trip_selection(self, driver):
#         round_trip_radio = driver.find_element(By.XPATH, "//input[@value='ROUNDTRIP']")
#         round_trip_radio.click()
#         return_date_field = wait_for_element((By.XPATH, "//input[@placeholder='Return Date']"))
#         assert return_date_field.is_displayed(), "Return date field is not displayed"
#         print("Round-trip radio button functionality verified")
#
#     # testcases Case 3.1: Verify the "From" and "To" input fields
#     def test_from_to_fields(self):
#         from_field = driver.find_element(By.XPATH, "//input[@placeholder='From']")
#         to_field = driver.find_element(By.XPATH, "//input[@placeholder='To']")
#         from_field.send_keys("Delhi")
#         to_field.send_keys("Mumbai")
#         suggestion = wait_for_element((By.XPATH, "//ul[contains(@class, 'autoSuggestBox')]//li"))
#         assert suggestion.is_displayed(), "Valid suggestions are not appearing"
#         print("From and To fields are working with suggestions")
#
#     # testcases Case 4.1: Verify the "Departure" date picker
#     def test_departure_date_picker(self):
#         departure_date_field = driver.find_element(By.XPATH, "//input[@placeholder='Departure Date']")
#         departure_date_field.click()
#         date = wait_for_element(
#             (By.XPATH, "//div[@aria-label='Wed Jun 12 2024']"))  # Adjust based on the available date
#         date.click()
#         selected_date = departure_date_field.get_attribute("value")
#         assert selected_date, "Departure date is not selected"
#         print("Departure date picker functionality verified")
#
#     # testcases Case 5.1: Verify the "Travellers & Class" dropdown
#     def test_travellers_class_dropdown(self):
#         travellers_class_dropdown = driver.find_element(By.XPATH, "//input[@placeholder='Travellers & Class']")
#         travellers_class_dropdown.click()
#         adult_increase_button = wait_for_element((By.XPATH, "//button[contains(@class, 'adultIncrease')]"))
#         adult_increase_button.click()
#         selected_adults = driver.find_element(By.XPATH, "//input[@name='adults']").get_attribute("value")
#         assert selected_adults == "2", "Travellers & Class dropdown is not working"
#         print("Travellers & Class dropdown functionality verified")
#
#     # testcases Case 6.1: Verify the "Special Fares" checkboxes
#     def test_special_fares_checkboxes(self):
#         special_fares = [
#             "//label[contains(text(), 'Student')]/preceding-sibling::input",
#             "//label[contains(text(), 'Senior Citizen')]/preceding-sibling::input",
#             "//label[contains(text(), 'Armed Forces')]/preceding-sibling::input",
#             "//label[contains(text(), 'Doctors & Nurses')]/preceding-sibling::input"
#         ]
#         for fare_xpath in special_fares:
#             checkbox = driver.find_element(By.XPATH, fare_xpath)
#             checkbox.click()
#             assert checkbox.is_selected(), "Special fare checkbox is not selectable"
#             checkbox.click()  # Deselect
#             assert not checkbox.is_selected(), "Special fare checkbox is not deselectable"
#         print("Special fares checkboxes functionality verified")
#
#     # testcases Case 7.1: Verify the "Search Flights" button functionality
#     def test_search_flights_button(self):
#         from_field = driver.find_element(By.XPATH, "//input[@placeholder='From']")
#         to_field = driver.find_element(By.XPATH, "//input[@placeholder='To']")
#         from_field.send_keys("Delhi")
#         to_field.send_keys("Mumbai")
#         wait_for_element((By.XPATH, "//ul[contains(@class, 'autoSuggestBox')]//li")).click()  # Select suggestion
#         departure_date_field = driver.find_element(By.XPATH, "//input[@placeholder='Departure Date']")
#         departure_date_field.click()
#         wait_for_element(
#             (By.XPATH, "//div[@aria-label='Wed Jun 12 2024']")).click()  # Adjust based on the available date
#         search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'SEARCH FLIGHTS')]")
#         search_button.click()
#         search_results = wait_for_element((By.XPATH, "//div[contains(@class, 'searchResults')]"))
#         assert search_results.is_displayed(), "Search results are not displayed"
#         print("Search Flights button functionality verified")
