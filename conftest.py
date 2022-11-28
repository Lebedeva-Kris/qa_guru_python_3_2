import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_webdriver_config():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver


@pytest.fixture()
def set_browser_size(set_webdriver_config):
    browser.config.driver.maximize_window()


@pytest.fixture()
def open_browser(set_webdriver_config, set_browser_size):
    b = browser.open('https://google.com')
    print("Браузер открыт")
    yield b
    print("Браузер закрыт!")
