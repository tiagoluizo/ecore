import sys
import os

# Add parent directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from helpers.webdriver_utils import get_chrome_driver, quit_driver
from pages.login_page import LoginPage


class TestInvalidLogin(unittest.TestCase):
   
    def setUp(self):
        self.driver = get_chrome_driver()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        quit_driver(self.driver)


    def test_login_invalid_credentials(self):
        # Open the login page
        self.login_page.open()

        # Define test data
        test_data = [
            {"username": "Demouser", "password": "abc123"},
            {"username": "demouser_", "password": "xyz"},
            {"username": "demouser", "password": "nananana"},
            {"username": "demouser", "password": "abc123"},
        ]

        for i, data in enumerate(test_data, start=1):
            # Perform login with invalid credentials
            self.login_page.login(data["username"], data["password"])

            # Verify error message is displayed
            error_message_displayed = self.login_page.is_error_message_displayed()
            self.assertTrue(error_message_displayed, f"Expected error message not displayed for Iteration {i}")

            # Clear the fields for the next iteration
            self.driver.refresh()


if __name__ == "__main__":
    unittest.main()
