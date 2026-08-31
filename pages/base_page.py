"""
Base page
(Page object model)
"""

from playwright.sync_api import Page, expect
from re import Pattern
import allure

#=======================================================================================================================
class BasePage:                                 # Родительский класс
    def __init__(self, page: Page):             # Конструктор класса, принимающий page
        self.page = page

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Open page
    @allure.step('⿹ Open page')
    def open(self, url: str):
        """
        ⿹ Open page

        - ▶ Open page

        :param url: Page URL
        """
        self.page.goto(url=url)

    # Reload page
    @allure.step('↺ Reload page {self.page.url}')
    def reload(self):
        """
        ↺ Reload current page

        .
        """
        self.page.reload()

    # Wait (timeout)
    @allure.step('...wait {timeout} sec')
    def wait(self, timeout: int = 2):
        """
        Wait (timeout) sec

        :param timeout: Timeout in sec (2 sec by default)
        """
        self.page.wait_for_timeout(timeout * 1000)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Current URL] - ⚠️Дублирование из BaseComponent
    @allure.step('✔ Check current page URL')
    def check_current_url(self, url: str | Pattern[str]):
        """
        ✔ Check [Current page URL]

        :param url: Expected page URL
        """
        error = f'❌ Current page URL - incorrect!'
        expect(self.page, error).to_have_url(url)


#=======================================================================================================================
