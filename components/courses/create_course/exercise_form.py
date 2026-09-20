"""
Create exercise form (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.input_field import InputField

#=======================================================================================================================
class CreateCourseExerciseFormComponent(BaseComponent):
    """
    Create exercise form (component)

    - Title input field
    - Description input field
    """
    PATH = 'Create course page > Exercises > Exercise > Form'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_input_field_locator(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input').locator('input')

    def description_input_field_locator(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input').locator('input')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title_input_field(self, index: int = 0) -> InputField:
        return InputField(self.title_input_field_locator(index), self.PATH, 'Title input field')

    def description_input_field(self, index: int = 0) -> InputField:
        return InputField(self.description_input_field_locator(index), self.PATH, 'Description input field')


    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------
    # Fill [Exercise form]
    @allure.step('▶ Fill [Exercise form]')
    def fill(self, title: str, description: str, index: int = 0):
        """
        ▶ Fill [Exercise form]

        - Title input field - ▶ fill
        - Description input field - ▶ fill

        :param title: Title
        :param description: Description
        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.title_input_field(index).fill(title)
        self.description_input_field(index).fill(description)


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Exercise form]
    # ────────────────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Exercise form]')
    def check(
        self,
        index: int = 0,
        title: str = 'Exercise title',
        description: str = 'Exercise description'
    ):
        """
        ✔ Check [Exercise form]

        - ✔ Title input field
        - ✔ Description input field

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title (Default: 'Exercise title')
        :param description: Exercise description (Default: 'Exercise description')
        """
        self.check_title_input_field(index, title)
        self.check_description_input_field(index, description)
    # ─────────────────────────────────────────────────────────────────────────┘

    # [Title input field]
    @allure.step('✔ Check [Title input field]')
    def check_title_input_field(self, index: int = 0, title: str = 'Exercise title'):
        """
        ✔ Check [Title input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - value (Default: 'Exercise title')

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title (optional)
        """
        self.title_input_field(index).check_visible()
        self.title_input_field(index).check_name(name='Title')
        self.title_input_field(index).check_value(title)

    # [Description input field]
    @allure.step('✔ Check [Description input field]')
    def check_description_input_field(self, index: int = 0, description: str = 'Exercise description'):
        """
        ✔ Check [Description input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - value (Default: 'Exercise description')

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Description (optional)
        """
        self.description_input_field(index).check_visible()
        self.description_input_field(index).check_name(name='Description')
        self.description_input_field(index).check_value(description)

#=======================================================================================================================
