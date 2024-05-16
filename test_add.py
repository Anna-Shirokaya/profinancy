from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from LoginPage import LoginActions
from WalletPage import WalletActions, WalletLocators as ll
from Fibbonachi import fibonacciDay
import re
import pytest

#accountName = 'Anna'


def test_login(browser):
    login_page = LoginActions(browser)
    login_page.go_to_site()
    login_page.login_with_valid_credentials('anna1038@yandex.ru', 'Unijuice04')
    login_page.click_login_button()
    
    wallet_page = WalletActions(browser)
    wallet_page.navigate()
    wallet_page.click_button(ll.create_account_button)
    wallet_page.fill_input(ll.account_name_input, 'Анна')
    wallet_page.fill_input(ll.currency_input, 'Российский рубль')
    wallet_page.set_image(ll.image_button, ll.paw_button)
    wallet_page.set_image(ll.color_button, ll.grey_button)
    wallet_page.click_button(ll.create_button)
    wallet_page.click_button(ll.add_operation_button)
    wallet_page.click_button(ll.income_tab)
    wallet_page.fill_input(ll.income_input, fibonacciDay)
    wallet_page.fill_input(ll.type_income_input, 'Зарплата')
    wallet_page.fill_input(ll.transaction_account_name_income_input, 'Anna')
    wallet_page.click_button(ll.create_transaction_button)
   
    wallet_page.click_button(ll.outcome_tab)
    wallet_page.fill_input(ll.outcome_input, fibonacciDay)
    wallet_page.fill_input(ll.type_outcome_input, 'Кофе')
    wallet_page.fill_input(ll.transaction_account_name_outcome_input, 'Anna')
    wallet_page.click_button(ll.create_transaction_button)

    resultbalance = wallet_page.balance(ll.balance)
    assert '0 ₽' == resultbalance.text
    






    

   
