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
    def get_locator(self, **kwargs) -> Locator:
        """
        ⚙ Переопределяет базовый get_locator() из BaseElement() для работы с <textarea> field

        <textarea> field имеет дополнительный .locator(на выбор):
        ----------------------------------------------------------
        - .locator('textarea:visible')
        - .locator('textarea').first

        :param kwargs: Additional named parameters for create locator
        :return: Locator (for <textarea> field)
        """
        locator = super().get_locator(**kwargs).locator('textarea:visible')  # Вызываем базовый (super) get_locator() и добавляем 'textarea:visible'
        return locator                                                       # Locator (for <textarea> fields)

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Fill]
    def fill(self, value: str, **kwargs):
        """
        ▶ Fill Field with value

        :param value: Value to fill
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(**kwargs)                   # инициализация локатора
        locator.fill(value)                                    # Playwright action

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Name]
    def check_name(self, name: str, **kwargs):                 # принимает именованные параметры для подстановки в шаблон
        """
        ✔ Check Field name

        :param name: Field expected name
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(**kwargs)                   # инициализация локатора
        error = f'❌ Field - incorrect name!'
        expect(locator, error).to_have_accessible_name(name)   # Playwright expect

    # [Placeholder]
    def check_placeholder(self, placeholder: str, **kwargs):
        """
        ✔ Check Field placeholder

        :param placeholder: Field expected placeholder
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(**kwargs)                                  # инициализация локатора
        error = f'❌ Field - incorrect placeholder!'
        expect(locator, error).to_have_attribute('placeholder', placeholder)  # Playwright expect

    # [Value]
    def check_value(self, value: str, **kwargs):
        """
        ✔ Check Field value

        :param value: Field expected value
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(**kwargs)                   # инициализация локатора
        error = f'❌ Field - incorrect value!'
        expect(locator, error).to_have_value(value)            # Playwright expect


#=======================================================================================================================
