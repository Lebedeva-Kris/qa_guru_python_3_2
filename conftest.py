import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_webdriver_config():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver



@pytest.fixture(scope="session")
def open_browser():
    b = browser.open('https://google.com')
    print("Браузер открыт")
    yield b
    print ("Браузер закрыт!")

@pytest.fixture(scope="session")
