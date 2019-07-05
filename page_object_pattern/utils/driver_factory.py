from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "firefox":
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        raise Exception("Provide valid driver name")
