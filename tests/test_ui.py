import allure
from python_sentinel_one import app


@allure.parent_suite('UI')
@allure.suite('Web')
@allure.title('Test request demo form')
@allure.link('https://www.sentinelone.com/request-demo/', name='Form page')
def test_get_demo_form():
    with allure.step('Open form page'):
        app.open_form_page('https://www.sentinelone.com/request-demo/')

    with allure.step('Fill form'):
        app.form.fill_first_name('Mrta')
        app.form.fill_last_name('Smth')
        app.form.fill_email('ycjojs@snova.io')
        app.form.fill_company('Sovja Mi')
        app.form.fill_mobile_phone('586-565-1292')
        app.form.choose_employees_number('50-500')
        app.form.choose_country('Costa Rica')
        app.form.submit()

    with allure.step('Check endpoint is reached'):
        app.endpoint.should_be('/request-demo-thank-you')

    app.add_attachments()
