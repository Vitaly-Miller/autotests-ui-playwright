"""
Courses list toolbar (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.button import Button
from elements.text import Text

#=======================================================================================================================
class CoursesListToolbarComponent(BaseComponent):
    """
    Courses list toolbar (component)

    - Title
    - Create course button
    """
    PATH = 'Courses list page > Toolbar'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('courses-list-toolbar-title-text')

    def create_course_btn_locator(self) -> Locator:
        return self.page.get_by_test_id('courses-list-toolbar-create-course-button')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.PATH, 'Title')

    def create_course_btn(self) -> Button:
        return Button(self.create_course_btn_locator(), self.PATH, 'Create course button')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Create course button]
    def click_create_course_btn(self):
        """
        ▶ Click [Create course button]

        .
        """
        self.create_course_btn().click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Toolbar]
    # ────────────────────────────────┐
    @allure.step('✔ Check [Toolbar]')
    def check(self):
        """
        ✔ Check [Toolbar]

        - ✔ Title
        - ✔ Create course button
        """
        self.check_title()
        self.check_create_course_btn()
    # ────────────────────────────────┘

    # [Title]
    @allure.step('✔ Check [Title]')
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.title().check_visible()
        self.title().check_text('Courses')

    # [Create course button]
    @allure.step('✔ Check [Create course button]')
    def check_create_course_btn(self):
        """
        ✔ Check [Create course button]

        - ✔ Button - visible
        """
        self.create_course_btn().check_visible()

#=======================================================================================================================
