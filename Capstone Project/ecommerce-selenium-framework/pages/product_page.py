from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
    # Locators
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div#content h1")
    PRICE = (By.CSS_SELECTOR, "ul.list-unstyled h2")
    CART_TOTAL_BUTTON = (By.ID, "cart-total")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_cart_to_update(self):
        """Wait until the cart total button indicates an item was added. Prevents empty cart sync issues."""
        # Wait up to 10 seconds for the cart total to NOT be "0 item(s)"
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(self.CART_TOTAL_BUTTON, "0 item(s)")
        )

    def set_quantity(self, qty):
        self.enter_text(self.QUANTITY_INPUT, str(qty))

    def click_add_to_cart(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(0.8)  

    def get_success_message(self):
        dedicated_wait = WebDriverWait(self.driver, 25)
        element = dedicated_wait.until(EC.visibility_of_element_located(self.SUCCESS_ALERT))
        return element.text

    def get_product_title(self):
        return self.get_element_text(self.PRODUCT_TITLE)

    def get_product_price(self):
        return self.get_element_text(self.PRICE)
