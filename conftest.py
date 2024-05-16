import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    # Опции для отключения запросов на уведомления
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()