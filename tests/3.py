import sys
import os

# Add parent directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium.webdriver.common.by import By
from helpers.webdriver_utils import get_chrome_driver, quit_driver
from pages.login_page import LoginPage
from pages.invoice_page import InvoicePage, InvoiceDetailsPage
from helpers.currency_utils import format_usd_currency

class TestInvoiceDetails(unittest.TestCase):
    def setUp(self):
        self.driver = get_chrome_driver()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        quit_driver(self.driver)


    def test_invoice_details(self):
        # Perform successful login
        self.login_page.open()
        self.login_page.login("demouser", "abc123")
        self.assertTrue(self.login_page.is_logged_in(), "Login failed.")

        # Click the Invoice Details link for the first item
        self.invoice_page = InvoicePage(self.driver)
        self.invoice_page.click_invoice_details()

        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Validate the information presented on the Invoice Details page
        expected_data = {
            "HotelName": "Rendezvous Hotel",
            "InvoiceDate": "14/01/2018",
            "DueDate": "15/01/2018",
            "InvoiceNumber": "110",
            "BookingCode": "0875",
            "CustomerDetails": "JOHNY SMITH\nR2, AVENUE DU MAROC\n123456",
            "Room": "Superior Double",
            "Checkin": "14/01/2018",
            "CheckOut": "15/01/2018",
            "TotalStayCount": "1",
            "TotalStayAmount": "$150",
            "DepositNow": "USD $20.90",
            "Tax&VAT": "USD $19.00",
            "TotalAmount": "USD $209.00"
        }

        self.invoice_details_page = InvoiceDetailsPage(self.driver)

        assertions = [
            ("HotelName", self.invoice_details_page.get_hotel_name(), expected_data["HotelName"]),
            ("InvoiceDate", self.invoice_details_page.get_invoice_date(), expected_data["InvoiceDate"]),
            ("DueDate", self.invoice_details_page.get_due_date(), expected_data["DueDate"]),
            ("InvoiceNumber", self.invoice_details_page.get_invoice_number(), expected_data["InvoiceNumber"]),
            ("BookingCode", self.invoice_details_page.get_booking_code(), expected_data["BookingCode"]),
            ("CustomerDetails", self.invoice_details_page.get_customer_details(), expected_data["CustomerDetails"]),
            ("Room", self.invoice_details_page.get_room(), expected_data["Room"]),
            ("Checkin", self.invoice_details_page.get_checkin(), expected_data["Checkin"]),
            ("CheckOut", self.invoice_details_page.get_checkout(), expected_data["CheckOut"]),
            ("TotalStayCount", self.invoice_details_page.get_total_stay_count(), expected_data["TotalStayCount"]),
            ("TotalStayAmount", self.invoice_details_page.get_total_stay_amount(), expected_data["TotalStayAmount"]),
            ("DepositNow", self.invoice_details_page.get_deposit_now(), expected_data["DepositNow"]),
            ("Tax&VAT", self.invoice_details_page.get_tax_vat(), expected_data["Tax&VAT"]),
            ("TotalAmount", self.invoice_details_page.get_total_amount(), expected_data["TotalAmount"])
        ]
        failures = []
        for key, actual_value, expected_value in assertions:
            if key in ["TotalStayAmount", "DepositNow", "Tax&VAT", "TotalAmount"]:
                expected_value = expected_value.replace("$", "")  # Remove the "$" symbol
                expected_value = expected_value.split(" ")[-1]  # Extract the numeric part
                formatted_expected = format_usd_currency(float(expected_value))
            else:
                formatted_expected = expected_value

            try:
                self.assertEqual(actual_value, formatted_expected, f"Expected {key}: {formatted_expected}, but got {actual_value}")
            except AssertionError as e:
                failures.append(str(e))  # Collect the failure

        # Check if any failures occurred and report them
        if failures:
            failure_message = "\n\n".join(failures)
            self.fail(failure_message)




if __name__ == "__main__":
    unittest.main()
