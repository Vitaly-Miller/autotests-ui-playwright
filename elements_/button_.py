"""
Button element
(⚠️Page factory)
"""
import allure
from playwright.sync_api import expect
from elements_.base_element_ import BaseElement

#=======================================================================================================================
class Button(BaseElement):
    # Переопределенный метод
    @property
    def type_of(self) -> str:
        return 'button'

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Enabled]
    def check_enabled(self, nth_index: int = 0, **kwargs):                      # принимает именованные параметры для подстановки в шаблон
        """
        ✔ Check Button is enabled

        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index, **kwargs)                # инициализация локатора
        with allure.step(f'✔ Check [{self.name} {self.type_of}] is enabled'):   # Allure-step (динамический)
            error = f'❌ [{self.name} {self.type_of} (nth-index: {nth_index})] - disabled!'
            expect(locator, error).to_be_enabled()                              # Playwright expect

    # [Disabled]
    def check_disabled(self, nth_index: int = 0, **kwargs):                     # принимает именованные параметры для подстановки в шаблон
        """
        ✔ Check Button is disabled

        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index, **kwargs)                # инициализация локатора
        with allure.step(f'✔ Check [{self.name} {self.type_of}] is disabled'):   # Allure-step (динамический)
            error = f'❌ [{self.name} {self.type_of} (nth-index: {nth_index})] - enabled!'
            expect(locator, error).to_be_disabled()                             # Playwright expect


#=======================================================================================================================
