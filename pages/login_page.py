from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_page_url = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/"
        self.error_message = (By.CLASS_NAME, 'alert-danger')

        self.username_input = (By.NAME, 'username')
        self.password_input = (By.NAME, 'password')
        self.login_button = (By.ID, 'btnLogin')
        self.logout_link = (By.XPATH, '//a[@href="/logout"]')

    def open(self):
        self.driver.get(self.login_page_url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def is_page_loaded(self):
        try:
            self.driver.find_element(*self.username_input)
            return True  # Username input found, page is loaded
        except NoSuchElementException:
            return False
    
    def is_logged_in(self):
        try:
            self.driver.find_element(*self.logout_link)
            return True  # Logout link found, user is logged in
        except NoSuchElementException:
            return False
    def is_error_message_displayed(self):
        try:
            error_element = self.driver.find_element(*self.error_message)
            return error_element.is_displayed()
        except NoSuchElementException:
            return False