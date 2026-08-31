"""
Base check of element
"""
import allure
from playwright.sync_api import Locator, expect
from pathlib import Path

#=======================================================================================================================
class BaseElement:
    def __init__(self, locator: Locator, path: str, name: str):
        """
        Initialize base element

        :param locator: Element locator
        :param path: Element navigate-path
        :param name: Element name
        """
        self.locator = locator
        self.path = path
        self.name = f'[{name}]'
        self.error = f'❌ {self.path} > {self.name}'

    # --------------------------------------------------- Directories --------------------------------------------------
    ROOT = Path(__file__).parent.parent      # 🗂️Project ROOT/
    TESTDATA = ROOT/'testdata'               # └─ 📁testdata/
    FILES = TESTDATA/'files'                 #    └─ 📁files/

    # ----------------------------------------------------- Helpers ----------------------------------------------------
    @staticmethod
    def _nth_info(nth: int) -> str:
        """
        (Helper) Returns nth-index / empty string for logging

        :param nth: nth-index of locator
        :return: str
        """
        return '' if nth == 0 else f' (nth: {nth})'


    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------
    # Click
    def click(self, nth: int = 0):
        """
        ▶ Click [Element]

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        with allure.step(f'▶ Click {self.name}{nth_info}'):
            self.locator.nth(nth).click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Visible
    def check_visible(self, nth: int = 0):
        """
        ✔ Check [Element] is visible

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        with allure.step(f'✔ Check {self.name}{nth_info} is visible'):
            error = f'{self.error}{nth_info} - invisible!'
            expect(self.locator.nth(nth), error).to_be_visible()


    # Hidden
    def check_hidden(self, nth: int = 0):
        """
        ✔ Check [Element] is hidden

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        with allure.step(f'✔ Check {self.name}{nth_info} is hidden'):
            error = f'{self.error}{nth_info} - visible!'
            expect(self.locator.nth(nth), error).to_be_hidden()


    # Text
    def check_text(self, text: str, nth: int = 0):
        """
        ✔ Check [Element] text

        :param text: Expected text
        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        with allure.step(f'✔ Check {self.name}{nth_info} text: "{text}"'):
            error = f'{self.error}{nth_info} - incorrect text!'
            expect(self.locator.nth(nth), error).to_have_text(text)

#=======================================================================================================================
