"""
Unittest Suite
==============
Demonstrates the Unittest framework requirement.
This file is named 'unittest_login.py' (without a 'test_' prefix) so that 
PyTest automatically ignores it. It is executed via 'python -m unittest' 
in the batch script.
"""

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage
from utilities.read_config import ReadConfig
import time

class TestLoginUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs once before all tests in this class."""
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.base_url = ReadConfig.get_base_url()
        cls.login_url = f"{cls.base_url}index.php?route=account/login"

    def setUp(self):
        """Runs before each test."""
        self.driver.get(self.login_url)
        self.login_page = LoginPage(self.driver)

    def test_01_valid_login(self):
        self.login_page.login(ReadConfig.get_valid_email(), ReadConfig.get_valid_password())
        self.assertTrue(self.login_page.is_login_successful(), "Valid login failed!")
        self.login_page.logout()

    def test_02_invalid_login(self):
        self.login_page.login("no_such_user@fake.com", "wrong_password")
        self.assertIn("Warning", self.login_page.get_error_message(), "Invalid login did not show warning!")

    def test_03_empty_credentials(self):
        self.login_page.login("", "")
        self.assertIn("Warning", self.login_page.get_error_message(), "Empty login did not show warning!")

    def tearDown(self):
        """Runs after each test to add a pause for the demo."""
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        """Runs once after all tests have completed."""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
