import logging
import allure
from allure_commons.types import AttachmentType


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        # Setting logger
        self.logger = logging.getLogger(__name__)

        # Page objects
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//*[@id='select2-drop']//input"
        self.location_match_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"

    # Allure test report decorator
    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        # Logs
        self.logger.info(f"Setting city {city}")

        # Activate "Search by hotel or city name" text box
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()

        # Type to "Search by hotel or city name" text box
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)

        # Click at proposed results
        self.driver.find_element_by_xpath(self.location_match_xpath).click()

        # Attach screenshot to Allure report
        allure.attach(self.driver.get_screenshot_as_png(), name="Set city", attachment_type=AttachmentType.PNG)

    # Allure test report decorator
    @allure.step("Setting date range from '{1}' to '{2}'")
    def set_date_range(self, check_in, check_out):
        # Logs
        self.logger.info(f"Setting checkin {check_in} and checkout {check_out} dates")

        # Set "Check in" date.
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)

        # Set "Check out" date.
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)

        # Attach screenshot to Allure report
        allure.attach(self.driver.get_screenshot_as_png(), name="Set date range", attachment_type=AttachmentType.PNG)

    # Allure test report decorator
    @allure.step("Setting travelers. Adults - '{1}', child - '{2}'")
    def set_travellers(self, adults, child):
        # Logs
        self.logger.info(f"Setting travellers. Adults - {adults} child - {child}")

        # Add adults
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adults)

        # Add children's
        self.driver.find_element_by_id(self.child_input_id).clear()
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)

        # Attach screenshot to Allure report
        allure.attach(self.driver.get_screenshot_as_png(), name="Set travelers", attachment_type=AttachmentType.PNG)

    # Allure test report decorator
    @allure.step("Perform search")
    def perform_search(self):
        # Logs
        self.logger.info(f"Performing search")

        # Click "Search" button
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

