"""
Create course page > [Toolbar]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.button import Button
from elements.text import Text

#=======================================================================================================================
class CreateCourseToolbarComponent(BaseComponent):
    """
    [Toolbar] component

    - Title
    - Create course button
    """
    path = 'Create course page > Toolbar'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-toolbar-title-text')

    def create_course_btn_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-toolbar-create-course-button')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.path, 'Title')

    def create_course_btn(self) -> Button:
        return Button(self.create_course_btn_locator(), self.path, 'Create course button')


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
    # ─────────────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Toolbar]')
    def check(self, create_course_btn_enabled: bool = False):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Create course button - visible | - enabled / disabled

        :param create_course_btn_enabled: True / False
        """
        self.check_title()
        self.check_create_course_btn(enabled=create_course_btn_enabled)
    # ─────────────────────────────────────────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.check_title_visible()
        self.check_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_title_visible(self):
        """
        ✔ Check [Title] is visible

        .
        """
        self.title().check_visible()

    # Text
    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        self.title().check_text('Create course')


    # [Create course button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Create course button]')
    def check_create_course_btn(self, enabled: bool = False):
        """
        ✔ Check [Create course button]

        - ✔ Button - visible
        - ✔ Button - enabled / disabled
        """
        self.check_create_course_btn_visible()
        if enabled:
            self.check_create_course_btn_enabled()
        else:
            self.check_create_course_btn_disabled()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_create_course_btn_visible(self):
        """
        ✔ Check [Create course button] is visible

        .
        """
        self.create_course_btn().check_visible()

    # Enabled
    def check_create_course_btn_enabled(self):
        """
        ✔ Check [Create course button] is enabled

        (If create course Form filled & Image uploaded)
        """
        self.create_course_btn().check_enabled()

    # Disabled
    def check_create_course_btn_disabled(self):
        """
        ✔ Check [Create course button] disabled

        (If create course Form did NOT filled & Image did NOT upload)
        """
        self.create_course_btn().check_disabled()


#=======================================================================================================================
