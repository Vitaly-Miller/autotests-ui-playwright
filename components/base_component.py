"""
BASE component
(Page component)
"""

import allure
from playwright.sync_api import Page, expect
from pathlib import Path
from re import Pattern

#=======================================================================================================================
class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Current URL]
    @allure.step('✔ Check current page URL')
    def check_current_url(self, url: str | Pattern[str]):
        """
        ✔ Check [Current page URL]

        :param url: Expected page URL
        """
        error = f'❌ Current page URL - incorrect!'
        expect(self.page, error).to_have_url(url)

#=======================================================================================================================
