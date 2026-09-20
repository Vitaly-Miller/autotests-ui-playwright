"""
Exercises toolbar (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.button import Button
from elements.text import Text

#=======================================================================================================================
class CreateCourseExercisesToolbarComponent(BaseComponent):
    """
    Exercises toolbar (component)

    - Title
    - Create exercise button
    """
    PATH = 'Create course page > Exercises > Toolbar'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-exercises-box-toolbar-title-text')

    def create_exercise_btn_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.PATH, 'Title')

    def create_exercise_btn(self) -> Button:
        return Button(self.create_exercise_btn_locator(), self.PATH, 'Create exercise button')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Create exercise button]
    def click_create_exercise_btn(self):
        """
        ▶ Click [Create exercise button]

        .
        """
        self.create_exercise_btn().click()

    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # [Toolbar]
    # ──────────────────────────────────┐
    @allure.step('✔ Check [Toolbar]')
    def check(self):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Create exercise button - visible
        """
        self.check_title()
        self.check_create_exercise_btn()
    # ──────────────────────────────────┘

    # [Title]
    @allure.step('✔ Check [Title]')
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.title().check_visible()
        self.title().check_text('Exercises')

    # [Create exercise button]
    @allure.step('✔ Check [Create exercise button]')
    def check_create_exercise_btn(self):
        """
        ✔ Check [Create exercise button]

        - ✔ Button - visible
        """
        self.create_exercise_btn().check_visible()


#=======================================================================================================================
