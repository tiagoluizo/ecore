from selenium.webdriver.common.by import By
from helpers.currency_utils import format_usd_currency


class InvoicePage:
    def __init__(self, driver):
        self.driver = driver
        self.invoice_details_links = (By.XPATH, '//a[text()="Invoice Details"]')

    def click_invoice_details(self, index=0):
        self.driver.find_elements(*self.invoice_details_links)[index].click()

class InvoiceDetailsPage:
    def __init__(self, driver):
        self.driver = driver

        # Element locators
        self.hotel_name = (By.CSS_SELECTOR, 'h4')
        self.invoice_number = (By.CSS_SELECTOR, '.mt-2')
        self.invoice_date = (By.CSS_SELECTOR, "body > section:nth-child(2) > div:nth-child(1) > ul:nth-child(5) > li:nth-child(1)")
        self.due_date = (By.CSS_SELECTOR, 'body > section:nth-child(2) > div:nth-child(1) > ul:nth-child(5) > li:nth-child(2)')
        self.booking_code = (By.XPATH, '//td[contains(text(), "Booking Code")]/following-sibling::td[1]')
        self.room = (By.XPATH, '//td[contains(text(), "Room")]/following-sibling::td[1]')
        self.total_stay_count = (By.XPATH, '//td[contains(text(), "Total Stay Count")]/following-sibling::td[1]')
        self.total_stay_amount = (By.XPATH, '//td[contains(text(), "Total Stay Amount")]/following-sibling::td[1]')
        self.checkin = (By.XPATH, '//td[contains(text(), "Check-In")]/following-sibling::td[1]')
        self.checkout = (By.XPATH, '//td[contains(text(), "Check-Out")]/following-sibling::td[1]')
        self.customer_details = (By.XPATH, '//h5[contains(text(), "Customer Details")]/following-sibling::div')
        self.deposit_now = (By.CSS_SELECTOR, 'body > section:nth-child(2) > div:nth-child(1) > table:nth-child(12) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')
        self.tax_vat = (By.CSS_SELECTOR, 'body > section:nth-child(2) > div:nth-child(1) > table:nth-child(12) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
        self.total_amount = (By.CSS_SELECTOR, 'body > section:nth-child(2) > div:nth-child(1) > table:nth-child(12) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')

    def get_hotel_name(self):
        return self.driver.find_element(*self.hotel_name).text

    def get_invoice_number(self):
        invoice_number = self.driver.find_element(*self.invoice_number).text
        number = invoice_number.split("#")[1].split()[0]
        return number

    def get_invoice_date(self):
        element = self.driver.find_element(*self.invoice_date)
        text = element.get_attribute('textContent')
        invoice_date = text.split(':')[-1].strip()
        return invoice_date


    def get_due_date(self):
        element = self.driver.find_element(*self.due_date)
        text = element.get_attribute('textContent')
        due_date = text.split(':')[-1].strip()
        return due_date

    def get_booking_code(self):
        return self.driver.find_element(*self.booking_code).text

    def get_room(self):
        return self.driver.find_element(*self.room).text

    def get_total_stay_count(self):
        return self.driver.find_element(*self.total_stay_count).text

    def get_total_stay_amount(self):
        amount = self.driver.find_element(*self.total_stay_amount).text
        numeric_amount = amount.split("$")[1].strip()
        formatted_amount = format_usd_currency(float(numeric_amount))
        return formatted_amount

    def get_checkin(self):
        return self.driver.find_element(*self.checkin).text

    def get_checkout(self):
        return self.driver.find_element(*self.checkout).text

    def get_customer_details(self):
        return self.driver.find_element(*self.customer_details).text

    def get_deposit_now(self):
        amount = self.driver.find_element(*self.deposit_now).text
        numeric_amount = amount.split("$")[1].strip()
        formatted_amount = format_usd_currency(float(numeric_amount))
        return formatted_amount

    def get_tax_vat(self):
        amount = self.driver.find_element(*self.tax_vat).text
        numeric_amount = amount.split("$")[1].strip()
        formatted_amount = format_usd_currency(float(numeric_amount))
        return formatted_amount

    def get_total_amount(self):
        amount = self.driver.find_element(*self.total_amount).text
        numeric_amount = amount.split("$")[1].strip()
        formatted_amount = format_usd_currency(float(numeric_amount))
        return formatted_amount