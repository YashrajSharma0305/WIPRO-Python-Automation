"""
Master E2E Journey
==================
This test file executes the entire E-Commerce flow serially in a single browser window.
It is highly organized and ensures no redundant logins/logouts.

Flow:
1. Negative Login (Data-Driven from CSV)
2. Valid Login
3. Search Product & View Details
4. Add to Cart & Checkout Verification
5. Clear Cart & Logout
"""

import pytest
import time
import os
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utilities.read_config import ReadConfig
from utilities.custom_logger import LogGen
from utilities.read_data import read_csv_data

logger = LogGen.loggen()

@pytest.mark.usefixtures("setup")
class TestMasterJourney:
    base_url = ReadConfig.get_base_url()
    login_url = f"{base_url}index.php?route=account/login"

    # --- STEP 1: NEGATIVE LOGIN ---
    def test_01_invalid_login(self):
        """Demonstrates Negative Testing by attempting a login with fake credentials."""
        logger.info("--- STEP 1: Negative Login Attempt ---")
        self.driver.get(self.login_url)
        login_page = LoginPage(self.driver)
        
        data_file = os.path.join(os.path.dirname(__file__), "..", "test_data", "login_data.csv")
        csv_data = read_csv_data(data_file)
        fake_email, fake_password, _ = csv_data[0] 

        login_page.login(fake_email, fake_password)
        error_msg = login_page.get_error_message()
        assert "Warning" in error_msg, "Expected warning for invalid login!"
        logger.info("Negative login successfully blocked by the application.")
        
        login_page.take_screenshot("01_Invalid_Credentials")

    # --- STEP 2: POSITIVE LOGIN ---
    def test_02_valid_login(self):
        """Logs into the application with valid credentials from config.ini."""
        logger.info("--- STEP 2: Valid Login ---")
        self.driver.get(self.login_url)
        login_page = LoginPage(self.driver)
        
        login_page.login(
            ReadConfig.get_valid_email(),
            ReadConfig.get_valid_password()
        )
        assert login_page.is_login_successful(), "Failed to login with valid credentials!"
        logger.info("Successfully logged into the real account.")
        

    # --- STEP 3: SEARCH & VIEW PRODUCT ---
    def test_03_search_and_view_product(self):
        """Searches for multiple products from CSV, then navigates to MacBook details page."""
        logger.info("--- STEP 3: Search and View Product (Data-Driven) ---")
        home_page = HomePage(self.driver)
        search_results = SearchResultsPage(self.driver)
        
        
        search_csv = os.path.join(os.path.dirname(__file__), "..", "test_data", "search_data.csv")
        search_items = read_csv_data(search_csv)
        
        for item in search_items:
            product_name = item[0]
            logger.info(f"Searching for: {product_name}")
            home_page.search_product(product_name)
            time.sleep(1) 
            
            home_page.take_screenshot(f"02_Search_Result_{product_name.replace(' ', '_')}")
        
        logger.info("Re-searching for MacBook to continue the flow...")
        home_page.search_product("MacBook")
        search_results.click_product("MacBook")
        
        product_page = ProductPage(self.driver)
        assert "MacBook" in product_page.get_product_title(), "Did not land on MacBook page!"
        logger.info("Successfully navigated to MacBook product page.")

    # --- STEP 4: ADD TO CART ---
    def test_04_add_to_cart(self):
        """Adds the product to the cart and verifies it appears in the checkout page."""
        logger.info("--- STEP 4: Add to Cart ---")
        product_page = ProductPage(self.driver)
        product_page.set_quantity(1)
        product_page.click_add_to_cart()
        
        success_msg = product_page.get_success_message()
        assert "Success" in success_msg, "Success banner did not appear!"
        
        
        product_page.wait_for_cart_to_update()
        
        self.driver.get(f"{self.base_url}index.php?route=checkout/cart")
        cart_page = CartPage(self.driver)
        assert cart_page.is_product_in_cart("MacBook"), "MacBook was not found in the cart!"
        logger.info("Product successfully added and verified in the cart.")
        
        cart_page.take_screenshot("03_Shopping_Cart_With_Item")

    # --- STEP 5: CLEANUP & LOGOUT ---
    def test_05_clear_cart_and_logout(self):
        """Clears the cart to keep the account clean, then logs out."""
        logger.info("--- STEP 5: Cleanup and Logout ---")
        self.driver.get(f"{self.base_url}index.php?route=checkout/cart")
        cart_page = CartPage(self.driver)
        
        cart_page.clear_cart()
        assert cart_page.is_cart_empty(), "Failed to clear the cart!"
        logger.info("Cart cleared successfully.")
        
        login_page = LoginPage(self.driver)
        login_page.logout()
        logger.info("Logged out safely. End of journey.")
