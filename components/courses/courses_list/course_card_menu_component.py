"""
Courses list page > Course card > [Menu] (component)
"""
import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
[Menu]:
- Edit button
- Delete button
"""
class CourseCardMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.EDIT_BTN_TEXT = 'Edit'
        self.DELETE_BTN_TEXT = 'Delete'

        # ------------------------------------ Elements (path & name) (for debug) --------------------------------------
        self.menu_component = '❌ Courses list page > Course card > Menu'
        self.edit_btn_element = lambda nth_index: f'{self.menu_component} > [Edit button] (nth_index: {nth_index})'
        self.delete_btn_element = lambda nth_index: f'{self.menu_component} > [Delete button] (nth_index: {nth_index})'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.edit_btn_locator = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_btn_locator = page.get_by_test_id('course-view-delete-menu-item')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Edit button]
    @allure.step('▶ Click [Edit button]')
    def click_edit_btn(self, nth_index: int = 0):
        """
        ▶ Click [Edit button]

        - ✔ Edit button - visible
        - ▶ Edit button - click

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        self.check_edit_btn_visible(nth_index)
        self.edit_btn_locator.nth(nth_index).click()


    # Click [Delete button]
    @allure.step('▶ Click [Delete button]')
    def click_delete_btn(self, nth_index: int = 0):
        """
        ▶ Click [Delete button]

        - ✔ Delete button - visible
        - ▶ Delete button - click

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        self.check_delete_btn_visible(nth_index)
        self.delete_btn_locator.nth(nth_index).click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Edit button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Edit button]')
    def check_edit_btn(self, nth_index: int = 0):
        """
        ✔ Check [Edit button]

        - ✔ Button - visible
        - ✔ Button - text

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        self.check_edit_btn_visible(nth_index)
        self.check_edit_btn_text(nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Edit button]')
    def check_edit_btn_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Edit button]

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'{self.edit_btn_element(nth_index)} - invisible!'
        expect(self.edit_btn_locator.nth(nth_index), error).to_be_visible()

    @allure.step('✔ Check text of [Edit button]')
    def check_edit_btn_text(self, nth_index: int = 0):
        """
        ✔ Check text of [Edit button]

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'{self.edit_btn_element(nth_index)} - incorrect text!'
        expect(self.edit_btn_locator.nth(nth_index), error).to_have_text(self.EDIT_BTN_TEXT)


    # [Delete button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Delete button]')
    def check_delete_btn(self, nth_index: int = 0):
        """
        ✔ Check [Delete button]

        - ✔ Button - visible
        - ✔ Button - text

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        self.check_delete_btn_visible(nth_index)
        self.check_delete_btn_text(nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Delete button]')
    def check_delete_btn_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Delete button]

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'{self.delete_btn_element(nth_index)}  - invisible!'
        expect(self.delete_btn_locator.nth(nth_index), error).to_be_visible()

    @allure.step('✔ Check text of [Delete button]')
    def check_delete_btn_text(self, nth_index: int = 0):
        """
        ✔ Check text of [Delete button]

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'{self.delete_btn_element(nth_index)} - incorrect text!'
        expect(self.delete_btn_locator.nth(nth_index), error).to_have_text(self.DELETE_BTN_TEXT)


#=======================================================================================================================
