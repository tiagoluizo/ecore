import sys
import os

# Add parent directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from helpers.webdriver_utils import get_chrome_driver, quit_driver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = get_chrome_driver()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        quit_driver(self.driver)

    def test_login_successful(self):
        # Open the login page
        self.login_page.open()
        self.assertTrue(self.login_page.is_page_loaded(), "Login page did not load successfully.")

        # Login with valid credentials
        self.login_page.login("demouser", "abc123")
        self.assertTrue(self.login_page.is_logged_in(), "Login failed.")

if __name__ == "__main__":
    unittest.main()
