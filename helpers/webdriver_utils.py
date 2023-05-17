from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_chrome_driver():
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def quit_driver(driver):
    driver.quit()
