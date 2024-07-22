import pytest
from selene import browser, be, have

@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_height = 844
    browser.config.window_width = 390
    yield
    browser.quit()

# @pytest.fixture()
# def negative_search():
#     browser.element('[name="text"]').should(be.blank).type('olololo').press_enter()
#     browser.element('[id="search"]').should(have.text('pumpum'))





