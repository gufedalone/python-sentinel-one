import allure
from selene import browser
from selene.support.conditions import have
from controls.dropdown import Dropdown


@allure.parent_suite('UI')
@allure.suite('Web')
@allure.title('Test request demo form')
@allure.link('https://www.sentinelone.com/request-demo/', name='Form page')
def test_get_demo_form():
    # GIVEN
    url = 'https://www.sentinelone.com/'

    with allure.step('Open main page'):
        browser.open(url)

    with allure.step('Cancel notifications'):
        browser.element('#onesignal-slidedown-cancel-button').click()

    # WHEN
    with allure.step('Open "request demo" form page'):
        browser.element('a.demo:nth-child(3)').click()

    with allure.step('Fill form'):
        browser.element('#FirstName').type('Marta')
        browser.element('#LastName').type('Smith')
        browser.element('.demo-form #Email').type('mycjojs@snova.io')
        browser.element('#Company').type('Snovja Mi')
        browser.element('#Phone').type('586-535-1202')
        Dropdown(browser.element('#Employees__c')).select(option='50-500')
        Dropdown(browser.element('#Country')).select(option='Costa Rica')
        browser.element('.demo-form button').click()

    # THEN
    with allure.step('Check verification message is shown'):
        browser.should(have.url_containing('/request-demo-thank-you'))
