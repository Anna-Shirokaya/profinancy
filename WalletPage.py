from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from conftest import browser
import time

class WalletLocators:
    create_account_button = (By.XPATH, '//button[span[text()="Создать счёт"]]')
    account_name_input = (By.XPATH, '//input[@placeholder="Введите название счета"]')
    currency_input = (By.CLASS_NAME, 'style_input__ZS9sN')
    image_button = (By.CLASS_NAME, 'sc-bipthf')
    paw_button = (By.XPATH,"//img[@src='https://storage.yandexcloud.net/ru.profinansy-wallet-storage/media/upload/2023/02/03/XZ4lNkvfqLCyig.svg']")
    color_button = (By.CLASS_NAME, 'sc-idnGdr')
    grey_button = (By.XPATH, '// *[contains(@style, "background: rgb(137, 137, 137)")]')
    create_button = (By.XPATH, '//button[span="Создать"]')
    add_operation_button = (By.XPATH, '//button[span[text()="Добавить операцию"]]')
    income_tab = (By.XPATH, '//p[contains(@class,"TransactionSidebar___StyledP-sc-1s39v0x-0") and text()="Доход"]')
    outcome_tab = (By.XPATH, '//p[contains(@class,"TransactionSidebar___StyledP-sc-1s39v0x-0") and text()="Расход"]')
    income_input = (By.XPATH, '//div[contains(@class,"dIlFSW")]/input')
    outcome_input = (By.XPATH, '//div[contains(@class,"dIlFSW")]/input')
    type_income_input = (By.XPATH, '//p[text()="Название дохода"]/following-sibling::div/input')
    type_outcome_input = (By.XPATH, '//p[text()="На что потратили"]/following-sibling::div/input')
    transaction_account_name_income_input = (By.XPATH, '//p[text()="Куда начислены средства"]/following-sibling::div/input')
    transaction_account_name_outcome_input = (By.XPATH, '//p[text()="Откуда была произведена трата"]/following-sibling::div/input')
    create_transaction_button = (By.XPATH, f'//button[span[text()="Создать"]]') 
    balance = (By.CLASS_NAME, 'bWwdak')
    


class WalletActions(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self):
        self.driver.get('https://profinansy.ru/wallet/')

    def click_button(self, locator):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.visibility_of_element_located((locator)))
        self.driver.execute_script("arguments[0].click();", button)

    def fill_input(self, locator, value):
        wait = WebDriverWait(self.driver, 10)
        input = wait.until(EC.visibility_of_element_located((locator)))
        input.send_keys(value)

    def set_image(self, locator, value):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", button)
        button = wait.until(EC.visibility_of_element_located(value))
        self.driver.execute_script("arguments[0].click();", button)

    def balance(self, locator):
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        balance = wait.until(EC.visibility_of_element_located((locator)))
        time.sleep(1)
        return balance
