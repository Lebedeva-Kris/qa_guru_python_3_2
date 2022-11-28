import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def open_browser():
    b = browser.open('https://google.com')
    print("Браузер открыт")
    return b