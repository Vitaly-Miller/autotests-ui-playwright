"""
Base page
(Page object model)
"""

from playwright.sync_api import Page, expect
from re import Pattern


#=======================================================================================================================
class BasePage:                                 # Родительский класс
    def __init__(self, page: Page):             # Конструктор класса, принимающий page
        self.page = page

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Open page
    def visit(self, url: str):
        """
        ⿹ Open page

        - ▶ Open page

        :param url: Page URL
        """
        self.page.goto(url=url)

    # Reload page
    def reload(self):
        """
        ↺ Reload current page

        .
        """
        self.page.reload()

    # Wait (timeout)
    def wait(self, timeout: int = 2):
        """
        Wait (timeout)

        :param timeout: Timeout in sec (2 sec by default)
        """
        self.page.wait_for_timeout(timeout * 1000)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ⚠️Дублирование из BaseComponent
    # [Current URL]
    def check_current_url(self, expected_url: str | Pattern[str]):
        """
        ✔ Check [Current page URL]

        :param expected_url: Expected Page URL
        """
        error = f'❌ Current page URL - incorrect!'
        expect(self.page, error).to_have_url(expected_url)

#=======================================================================================================================
