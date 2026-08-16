"""
Button element
(⚠️Page factory)
"""

from playwright.sync_api import expect
from elements_.base_element_ import BaseElement

#=======================================================================================================================
class Button(BaseElement):

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Enabled]
    def check_enabled(self, **kwargs):                # принимает именованные параметры для подстановки в шаблон
        """
        ✔ Check Button is enabled

        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(**kwargs)          # инициализация локатора
        error = f'❌ Button - disabled!'
        expect(locator, error).to_be_enabled()        # Playwright expect

    # [Disabled]
    def check_disabled(self, **kwargs):               # принимает именованные параметры для подстановки в шаблон
        """
        ✔ Check Button is disabled

        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(**kwargs)          # инициализация локатора
        error = f'❌ Button - enabled!'
        expect(locator, error).to_be_disabled()       # Playwright expect


#=======================================================================================================================
