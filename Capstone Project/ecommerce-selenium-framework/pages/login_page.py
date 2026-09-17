from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert-danger")
    MY_ACCOUNT_HEADER = (By.XPATH, "//h2[text()='My Account']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)
        
    def is_login_successful(self):
        return self.is_element_displayed(self.MY_ACCOUNT_HEADER)

    def logout(self):
        """Navigate directly to logout URL — works regardless of page state."""
        self.driver.get("https://tutorialsninja.com/demo/index.php?route=account/logout")
