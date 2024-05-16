from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class LoginLocators:
    email_input = (By.NAME, 'email')
    password_input = (By.NAME, 'password')
    login_button = (By.XPATH, '//button[span[text()="Войти"]]')

class LoginActions(BasePage):
    def login_with_valid_credentials(self, email, password):
        self.accept_cookies()
        self.find_element(LoginLocators.email_input).send_keys(email)
        self.find_element(LoginLocators.password_input).send_keys(password)

    def click_login_button(self):
        self.find_element(LoginLocators.login_button).click()
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.url_changes(self.driver.current_url))

    def accept_cookies(self):
        try:
            cookie_agree_button = self.driver.find_element(By.XPATH, '//button[span[text()="Принимаю"]]')
            cookie_agree_button.click()
            print("Нажата кнопка Принимаю")
        except NoSuchElementException:
            ''

