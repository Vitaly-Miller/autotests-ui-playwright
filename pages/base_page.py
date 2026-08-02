"""
BASE PAGE
"""
from playwright.sync_api import Page, expect

#=======================================================================================================================
class BasePage:                                 # Родительский класс
    def __init__(self, page: Page):             # Конструктор класса, принимающий page
        self.page = page

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def visit(self, url: str):
        """
        ⿹ Open page

        - ▶ Open page
        - ✔ Page opened - successfully

        :param url: Page URL
        """
        self.page.goto(url=url)
        self.check_page_opened(expected_url=url)

    def reload(self):
        """
        ↺ Reload courant page

        .
        """
        self.page.reload()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_page_opened(self, expected_url: str):
        """
        Check Page opened successfully

        - ✔ Page opened - successfully. Page URL - correct.

        :param expected_url: Expected Page URL
        """
        error = '❌ Page did not opened! Page URL - incorrect!'
        expect(self.page, error).to_have_url(expected_url)

#=======================================================================================================================
