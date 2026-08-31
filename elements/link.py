"""
Link element
"""
import allure
from playwright.sync_api import expect
from elements.base_element import BaseElement

#=======================================================================================================================
class Link(BaseElement):
    """
    - ❌ НЕ ВЫЗЫВАТЬ НАПРЯМУЮ базовые методы из Родительского класса - BaseElement()!
    - ✅ Вызывать ТОЛЬКО ЧЕРЕЗ ЭТОТ Дочерний класс элемента!
    """
    # href (Hypertext Reference)
    def check_href(self, href: str, nth: int = 0):
        """
        ✔ Check [Link] "href" url-attribute

        :param href: "href" url-attribute
        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        with allure.step(f'✔ Check {self.name}{nth_info} "href": "{href}"'):
            error = f'{self.error}{nth_info} - incorrect "href" url-attribute!'
            expect(self.locator.nth(nth), error).to_have_attribute('href', href)


#=======================================================================================================================
