from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):
    PRODUCT_TITLES = (By.CSS_SELECTOR, "div.product-thumb h4 a")
    NO_RESULTS_MESSAGE = (By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_product_displayed(self, expected_product_name):
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        for element in elements:
            if expected_product_name.lower() in element.text.lower():
                return True
        return False
        
    def is_no_results_message_displayed(self):
        return self.is_element_displayed(self.NO_RESULTS_MESSAGE)
        
    def click_product(self, product_name):
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        for element in elements:
            if product_name.lower() in element.text.lower():
                element.click()
                return
        raise Exception(f"Product {product_name} not found in search results")
