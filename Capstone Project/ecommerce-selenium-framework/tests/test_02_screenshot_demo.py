"""
Screenshot on Failure Demo
===========================
Demonstrates the auto-screenshot capture feature.
"""
import pytest
from pages.home_page import HomePage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen

logger = LogGen.loggen()

@pytest.mark.usefixtures("setup")
class TestScreenshotDemo:
    base_url = ReadConfig.get_base_url()

    def test_99_screenshot_on_failure_demo(self):
        logger.info("--- STEP: Screenshot Demo ---")
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.search_product("Apple Car")

        search_results = HomePage(self.driver) 
        assert search_results.is_element_displayed(("xpath", "//a[text()='Apple Car']")), \
            "[INTENTIONAL FAILURE] Apple Car not found! Capturing screenshot..."
