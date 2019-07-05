import pytest
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_hotel_results import SearchHotelResultsPage
import allure

#  ___________________
# | RUN TEST + REPORT |
#  -------------------
# pytest --alluredir=/Users/hubertarciszewski/repo/selenium-projects/php-travels/page_object_pattern/reports --log-format="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)s) %(message)s"
#
#  ___________________
# | GENERATE REPORT   |
#  -------------------
# allure serve /Users/hubertarciszewski/repo/selenium-projects/php-travels/page_object_pattern/reports
#

# To run setup method before each test method in this class.
# We need use this decorator and pass method name.
@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    # Allure test report decorator
    @allure.title("Hotel search test")
    @allure.description("This is the description")
    # Test method
    def test_hotel_search(self):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("12/09/2019", "13/09/2019")
        search_hotel_page.set_travellers("2", "2")
        search_hotel_page.perform_search()
        result_page = SearchHotelResultsPage(self.driver)
        hotel_names = result_page.get_hotel_names()
        price_values = result_page.get_hotel_prices()

        # Assertions - Hotel names
        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        # Assertions - Prices
        assert price_values[0] == "$22"
        assert price_values[1] == "$50"
        assert price_values[2] == "$80"
        assert price_values[3] == "$150"





