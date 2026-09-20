"""
Exercise toolbar (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.button import Button
from elements.text import Text

#=======================================================================================================================
class CreateCourseExerciseToolbarComponent(BaseComponent):
    """
    Exercise toolbar (component)

    - Title
    - Delete exercise button
    """
    PATH = 'Create course page > Exercises > Exercise > Toolbar'

    # --------------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
    def title_locator(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')

    def delete_exercise_btn_locator(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')


    # --------------------------------------------------- ◈ ELEMENTS ---------------------------------------------------
    def title(self, index: int) -> Text:
        return Text(self.title_locator(index), self.PATH, 'Title')

    def delete_exercise_btn(self, index: int) -> Button:
        return Button(self.delete_exercise_btn_locator(index), self.PATH, 'Delete exercise button')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Delete exercise button]
    @allure.step('▶ Click [Delete exercise button]')
    def click_delete_exercise_btn(self, index: int):
        """
        ▶ Click [Delete exercise button]

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.delete_exercise_btn(index).click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Toolbar]
    # ───────────────────────────────────────┐
    @allure.step('✔ Check [Toolbar]')
    def check(self, index: int):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Delete exercise button - visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.check_toolbar_title(index)
        self.check_delete_exercise_btn(index)
    # ───────────────────────────────────────┘

    # [Title]
    @allure.step('✔ Check [Title]')
    def check_toolbar_title(self, index: int):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.title(index).check_visible()
        self.title(index).check_text(f'#{index + 1} Exercise')

    # [Delete exercise button]
    @allure.step('✔ Check [Delete exercise button]')
    def check_delete_exercise_btn(self, index: int):
        """
        ✔ Check [Delete exercise button]

        - ✔ Button - visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.delete_exercise_btn(index).check_visible()


#=======================================================================================================================
