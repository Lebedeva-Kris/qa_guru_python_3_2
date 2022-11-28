from selene.support.shared import browser
from selene import be, have


def test_body_positive(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="rcnt"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


def test_body_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('санагрварапупугандититини').press_enter()
    browser.element('[aria-level="3"]').should(have.text('По запросу санагрварапупугандититини ничего не найдено.'))
