import pytest
from selenium.webdriver.common.by import By
from Project.pages.FlightPage import FlightPage as flightpage

from Project.pages.BasePage import BasePage


@pytest.mark.parametrize('Locator', ['hello', 'hsjh', 'jhfks'])
@pytest.fixture(scope="class")
class Test_loginPage:
    # testcases Case 2.1: Verify that the "One-way" radio button is selected by default
    def test_one_way_selected(self, driver):
        one_way_radio = driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div/div/div[1]/ul/li[1]/span")
        assert one_way_radio.is_selected(), "One-way radio button is not selected by default"
        print("One-way radio button is selected by default")

    def test_search_one_way_tickets(self):
        flightpage.Click_From()
        flightpage.Enter_From_City("Delhi")
        flightpage.from_city_suggestions_xpath()
        flightpage.Click_Search()
