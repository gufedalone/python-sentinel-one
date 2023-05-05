from selene import browser
from selene.support.conditions import have


def should_be(value):
    browser.should(have.url_containing(value))
