"""
Create course page > Exercises > Exercise > [Form]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.input_field import InputField

#=======================================================================================================================
class CreateCourseExerciseFormComponent(BaseComponent):
    """
    [Form] component

    - Title field
    - Description field
    """
    PATH = 'Create course page > Exercises > Exercise > Form'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_field_locator(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

    def description_field_locator(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')

    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title_field(self, index: int = 0) -> InputField:
        return InputField(self.title_field_locator(index), self.PATH, 'Title field')

    def description_field(self, index: int = 0) -> InputField:
        return InputField(self.description_field_locator(index), self.PATH, 'Description field')

    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------
    # Fill [Exercise form]
    # ───────────────────────────────────────────────────────────────────┐
    @allure.step('▶ Fill [Exercise form]')
    def fill(self, title: str, description: str, index: int = 0):
        """
        ▶ Fill [Exercise form]

        - Title field - ▶ fill
        - Description field - ▶ fill

        :param title: Title
        :param description: Description
        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.fill_title_field(index=index, title=title)
        self.fill_description_field(index=index, description=description)
    # ───────────────────────────────────────────────────────────────────┘
    # Fill [Title field]
    def fill_title_field(self, title: str, index: int = 0):
        """
        ▶ Fill [Title field]

        :param title: Title
        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.title_field(index).fill(title)

    # Fill [Description field]
    def fill_description_field(self, description: str, index: int = 0):
        """
        ▶ Fill [Description field]

        :param description: Description
        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.description_field(index).fill(description)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Exercise form]
    # ────────────────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Exercise form]')
    def check(
        self,
        index: int = 0,
        title: str | None = None,
        description: str | None = None
    ):
        """
        ✔ Check [Exercise form]

        - ✔ Title field - value / UI
        - ✔ Description field - value / UI

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title (optional)
        :param description: Exercise description (optional)
        """
        self.check_title_field(index=index, title=title)
        self.check_description_field(index=index, description=description)
    # ────────────────────────────────────────────────────────────────────────┘

    # [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title field]')
    def check_title_field(self, index: int = 0, title: str | None = None):
        """
        ✔ Check [Title field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title (optional)
        """
        if title is not None:
            self.check_title_field_value(index=index, title=title)
        else:
            self.check_title_field_visible(index)
            self.check_title_field_name(index)
            self.check_title_field_value(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_title_field_visible(self, index: int = 0):
        """
        ✔ Check [Title field] is visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.title_field(index).check_visible()

    # Name
    def check_title_field_name(self, index: int = 0):
        """
        ✔ Check [Title field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.title_field(index).check_name(name='Title')

    # Value
    def check_title_field_value(self, index: int = 0, title: str = 'Exercise title'):
        """
        ✔ Check [Title field] value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title (default: 'Exercise title')
        """
        self.title_field(index).check_value(value=title)


    # [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Description field]')
    def check_description_field(self, index: int = 0, description: str | None = None):
        """
        ✔ Check [Description field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Description (optional)
        """
        if description is not None:
            self.check_description_field_value(index=index, description=description)
        else:
            self.check_description_field_visible(index)
            self.check_description_field_name(index)
            self.check_description_field_value(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_description_field_visible(self, index: int = 0):
        """
        ✔ Check [Description field] is visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.description_field(index).check_visible()

    # Name
    def check_description_field_name(self, index: int = 0):
        """
        ✔ Check [Description field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.description_field(index).check_name(name='Description')

    # Value
    def check_description_field_value(self, index: int = 0, description: str = 'Exercise description'):
        """
        ✔ Check [Description field] value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description (default: 'Exercise description')
        """
        self.description_field(index).check_value(value=description)

#=======================================================================================================================
