"""
Base component
"""

from playwright.sync_api import Page, expect
from re import Pattern

#=======================================================================================================================
class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ⚠️ ДУБЛИКАТ из BasePage - решить
    def check_current_url(self, expected_url: str | Pattern[str]):
        """
        Check Current page URL

        - ✔ Current page URL - correct

        :param expected_url: Expected Page URL
        """
        error = f'❌ Current page URL - incorrect!'
        expect(self.page, error).to_have_url(expected_url)


#=======================================================================================================================
