"""
BASE PAGE
"""

from playwright.sync_api import Page, expect
from pathlib import Path
from re import Pattern


#=======================================================================================================================
class BasePage:                                 # Родительский класс
    def __init__(self, page: Page):             # Конструктор класса, принимающий page
        self.page = page

    # -------------------------------------------------- Directories ---------------------------------------------------
    PROJECT = Path(__file__).parent.parent      # 🗂️Project ROOT/
    TESTDATA = PROJECT/'testdata'               # └─ 📁testdata/
    FILES = TESTDATA/'files'                    #    └─ 📁files/


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def visit(self, url: str):
        """
        ⿹ Open page

        - ▶ Open page

        :param url: Page URL
        """
        self.page.goto(url=url)

    def reload(self):
        """
        ↺ Reload current page

        .
        """
        self.page.reload()

    def wait(self, timeout: int = 2):
        """
        Wait 2 sec. (by default)

        :param timeout: Timeout in sec
        """
        self.page.wait_for_timeout(timeout * 1000)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_current_url(self, expected_url: str | Pattern[str]):
        """
        Check Current page URL

        - ✔ Current page URL - correct

        :param expected_url: Expected Page URL
        """
        error = f'❌ Current page URL - incorrect!'
        expect(self.page, error).to_have_url(expected_url)

#=======================================================================================================================
