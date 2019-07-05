import logging
import allure
from allure_commons.types import AttachmentType


class SearchHotelResultsPage:

    def __init__(self, driver):
        self.driver = driver
        # Logs
        self.logger = logging.getLogger(__name__)

        # Page objects
        self.hotel_names_xpath = "//h4[contains(@class,'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class,'price_tab')]//b"

    # Allure test report decorator
    @allure.step("Checking results")
    # Results - Get Hotel names
    def get_hotel_names(self):
        hotels = self.driver.find_elements_by_xpath(self.hotel_names_xpath)
        hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]

        # Attach screenshot to Allure report
        allure.attach(self.driver.get_screenshot_as_png(), name="Results", attachment_type=AttachmentType.PNG)

        # Log
        self.logger.info("Available hotels are: ")
        for name in hotel_names:
            self.logger.info(name)

        return hotel_names

    # Results - Get Hotel prices
    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]

        # Log
        self.logger.info("Prices are: ")
        for price in hotel_prices:
            self.logger.info(price)

        return hotel_prices
