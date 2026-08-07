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
        ↺ Reload courant page

        .
        """
        self.page.reload()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_current_url(self, expected_url: str | Pattern[str]):
        """
        Check Current page URL

        - ✔ Current page URL - correct

        :param expected_url: Expected Page URL
        """
        error = '❌ Current page URL - incorrect!'
        expect(self.page, error).to_have_url(expected_url)

#=======================================================================================================================
