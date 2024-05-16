from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from baseElements import Button

class BasePage:


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.login_url = "https://profinansy.ru/login/"

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    def go_to_site(self):
        return self.driver.get(self.login_url)
        
        
