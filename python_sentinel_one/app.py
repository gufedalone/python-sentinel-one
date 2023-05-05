import allure
from selene import browser
from controls import endpoint
from python_sentinel_one.pages.get_demo_page import GetDemoForm
from utils import attach

form = GetDemoForm()


def open_form_page(url: str):
    browser.open(url)
    with allure.step('Cancel notifications'):
        browser.element('#onesignal-slidedown-cancel-button').click()


def add_attachments():
    attach.add_screenshot()
    attach.add_logs()
    attach.add_html()
