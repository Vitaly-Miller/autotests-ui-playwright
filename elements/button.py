"""
Button element
"""
import allure
from playwright.sync_api import expect
from elements.base_element import BaseElement

#=======================================================================================================================
class Button(BaseElement):
    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # Enabled
    def check_enabled(self, nth: int = 0):
        """
        ✔ Check [Button] is enabled

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        with allure.step(f'✔ Check {self.name}{nth_info} is enabled'):
            error = f'{self.error}{nth_info} - disabled!'
            expect(self.locator.nth(nth), error).to_be_enabled()


    # Disabled
    def check_disabled(self, nth: int = 0):
        """
        ✔ Check [Button] is disabled

        :param nth: nth-index of locator
        """
        nth_info = self._nth_info(nth)
        with allure.step(f'✔ Check {self.name}{nth_info} is disabled'):
            error = f'{self.error}{nth_info} - enabled!'
            expect(self.locator.nth(nth), error).to_be_disabled()


#=======================================================================================================================
