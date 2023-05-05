import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.window_width, browser.config.window_height = 1920, 1080
    browser.config.hold_browser_open = True
    browser.config.timeout = 10
    yield browser
    browser.quit()
