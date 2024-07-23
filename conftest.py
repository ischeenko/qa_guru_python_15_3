import pytest
from selene import browser, be, have


@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_height = 844
    browser.config.window_width = 390
    yield
    browser.quit()

