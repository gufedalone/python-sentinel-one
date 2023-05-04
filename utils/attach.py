import allure
from allure_commons.types import AttachmentType


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(body=log, name='browser_logs', attachment_type=AttachmentType.TEXT, extension='.log')


def add_page_source(browser):
    allure.attach(
        body=browser.driver.page_source, name='page_source',
        attachment_type=AttachmentType.HTML, extension='.html'
    )


def add_screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(), name='screenshot',
        attachment_type=AttachmentType.PNG, extension='.png'
    )
