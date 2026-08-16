"""
BASE component
(Page component)
"""

from playwright.sync_api import Page, expect
from pathlib import Path
from re import Pattern

#=======================================================================================================================
class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    # -------------------------------------------------- Directories ---------------------------------------------------
    PROJECT = Path(__file__).parent.parent      # 🗂️Project ROOT/
    TESTDATA = PROJECT/'testdata'               # └─ 📁testdata/
    FILES = TESTDATA/'files'                    #    └─ 📁files/

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Current URL]
    def check_current_url(self, expected_url: str | Pattern[str]):
        """
        ✔ Check [Current page URL]

        :param expected_url: Expected Page URL
        """
        error = f'❌ Current page URL - incorrect!'
        expect(self.page, error).to_have_url(expected_url)


#=======================================================================================================================
