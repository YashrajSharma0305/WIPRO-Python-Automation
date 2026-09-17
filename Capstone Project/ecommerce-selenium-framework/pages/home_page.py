from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    # Locators
    MY_ACCOUNT_MENU = (By.CSS_SELECTOR, "a[title='My Account']")
    LOGIN_LINK = (By.XPATH, "//ul[contains(@class, 'dropdown-menu')]//a[contains(@href, 'account/login')]")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-btn button")

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_account(self):
        self.click_element(self.MY_ACCOUNT_MENU)

    def click_login(self):
        self.click_element(self.LOGIN_LINK)
        
    def navigate_to_login(self):
        self.click_my_account()
        self.click_login()

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click_element(self.SEARCH_BUTTON)
