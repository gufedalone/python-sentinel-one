from selene import browser
from controls.dropdown import Dropdown


class GetDemoForm:

    def __init__(self):
        self.employees = Dropdown(browser.element('#Employees__c'))
        self.country = Dropdown(browser.element('#Country'))
        self.state = Dropdown(browser.element('#State'))

    def fill_first_name(self, customer_name):
        browser.element('#FirstName').type(customer_name)
        return self

    def fill_last_name(self, customer_last_name):
        browser.element('#LastName').type(customer_last_name)
        return self

    def fill_email(self, customer_email):
        browser.element('.demo-form #Email').type(customer_email)
        return self

    def fill_company(self, company_name):
        browser.element('#Company').type(company_name)
        return self

    def fill_mobile_phone(self, phone):
        browser.element('#Phone').type(phone)
        return self

    def choose_employees_number(self, employees_number):
        self.employees.select(option=employees_number)
        return self

    def choose_country(self, country):
        self.employees.select(option=country)
        return self

    def submit(self):
        browser.element('.demo-form button').click()
        return self
