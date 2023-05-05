from selene.support.conditions import have
from selene.core.entity import Element
from selene.support.shared import browser


class Dropdown:

    def __init__(self, element: Element):
        self.element = element

    def select(self, /, *, option: str):
        browser.all('option').element_by(have.exact_text(option)).click()
