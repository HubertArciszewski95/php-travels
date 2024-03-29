import pytest
import allure
from allure_commons.types import AttachmentType
from page_object_pattern.utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    # Code to make screenshot when test fail
    before_failed = request.session.testsfailed
    # This will start after each test method. Because of "yield" keyword.
    yield
    # Code to make screenshot when test fail
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)

    driver.quit()
