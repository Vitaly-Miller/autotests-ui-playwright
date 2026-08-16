"""
Field <textarea> element
(⚠️Page factory)
"""
from elements_.base_element_ import BaseElement
from playwright.sync_api import Locator, expect

#=======================================================================================================================
class FieldTextarea(BaseElement):

    # --------------------------------------------------- ㉤ LOCATOR ----------------------------------------------------
    # [Locator] for <textarea> field (переопределенный из BaseElement())
    def get_locator(self, nth_index: int = 0, **kwargs) -> Locator:
        """
        ⚙ Переопределяет базовый get_locator() из BaseElement() для работы с <textarea> field

        <textarea> field имеет дополнительный .locator(на выбор):
        ----------------------------------------------------------
        - .locator('textarea:visible')
        - .locator('textarea').first

        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        :return: Locator (for <textarea> field)
        """
        locator = super().get_locator(nth_index=nth_index, **kwargs).locator('textarea:visible')  # Вызываем базовый (super) get_locator() и добавляем 'textarea:visible'
        return locator                                                              # Locator (for <textarea> fields)

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Fill]
    def fill(self, value: str, nth_index: int = 0, **kwargs):
        """
        ▶ Fill Field with value

        :param value: Value to fill
        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index=nth_index, **kwargs)                   # инициализация локатора
        locator.fill(value)                                                         # Playwright action

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Name]
    def check_name(self, name: str, nth_index: int = 0, **kwargs):                  # принимает именованные параметры для подстановки в шаблон
        """
        ✔ Check Field name

        :param name: Field expected name
        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index=nth_index, **kwargs)                   # инициализация локатора
        error = f'❌ Field - incorrect name!'
        expect(locator, error).to_have_accessible_name(name)                        # Playwright expect

    # [Placeholder]
    def check_placeholder(self, placeholder: str, nth_index: int = 0,  **kwargs):
        """
        ✔ Check Field placeholder

        :param placeholder: Field expected placeholder
        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index=nth_index, **kwargs)                   # инициализация локатора
        error = f'❌ Field - incorrect placeholder!'
        expect(locator, error).to_have_attribute('placeholder', placeholder)        # Playwright expect

    # [Value]
    def check_value(self, value: str, nth_index: int = 0,  **kwargs):
        """
        ✔ Check Field value

        :param value: Field expected value
        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index=nth_index, **kwargs)                   # инициализация локатора
        error = f'❌ Field - incorrect value!'
        expect(locator, error).to_have_value(value)                                 # Playwright expect


#=======================================================================================================================
