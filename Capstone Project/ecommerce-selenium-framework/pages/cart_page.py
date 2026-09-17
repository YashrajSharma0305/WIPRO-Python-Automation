from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    # Locators
    PRODUCT_NAMES = (By.CSS_SELECTOR, "div.table-responsive table tbody tr td:nth-child(2) a")
    CHECKOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Checkout') and @class='btn btn-primary']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your shopping cart is empty!')]")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "div.table-responsive table tbody button.btn-danger")

    def __init__(self, driver):
        super().__init__(driver)

    def get_products_in_cart(self):
        # Temporarily turn off implicit wait so it returns instantly if empty
        self.driver.implicitly_wait(0)
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        from utilities.read_config import ReadConfig
        self.driver.implicitly_wait(ReadConfig.get_implicit_wait()) # Restore
        return [element.text for element in elements]

    def is_product_in_cart(self, product_name):
        products = self.get_products_in_cart()
        return any(product_name.lower() in p.lower() for p in products)

    def click_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)

    def is_cart_empty(self):
        # A cart is empty if there are no products listed in the table
        return len(self.get_products_in_cart()) == 0
        
    def clear_cart(self):
        """Removes all items from the cart to keep the user account clean."""
        import time
        from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

        while True:
            try:
                remove_btns = self.driver.find_elements(*self.REMOVE_BUTTONS)
                if not remove_btns:
                    break
                # Click the first remove button
                remove_btns[0].click()
                time.sleep(2)  # Wait for the AJAX call to refresh the cart table
            except (NoSuchElementException, StaleElementReferenceException):
                # If DOM refreshed while we were checking, loop again
                time.sleep(1)
                continue
                
        if not self.is_cart_empty():
            self.driver.refresh()
            time.sleep(1)

