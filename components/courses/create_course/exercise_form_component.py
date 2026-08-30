"""
Create course page > Exercises > Exercise > [Form]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page
from elements.input_field import InputField

#=======================================================================================================================
"""
[Form]:
- Title field
- Description field
"""
class CreateCourseExerciseFormComponent(BaseComponent):
    # 𝌆 DATA
    TITLE_FIELD_NAME = 'Title'
    DESCRIPTION_FIELD_NAME = 'Description'

    def __init__(self, page: Page):
        super().__init__(page)

        # --------------------------------------- ㉧ LOCATORS {dynamic} (lambda) ----------------------------------------
        self.title_field_locator = lambda index: page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        self.description_field_locator = lambda index: page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')

        # ---------------------------------------- ◈ ELEMENTS {dynamic} (lambda) ---------------------------------------
        self.path = 'Create course page > Exercises > Exercise > Form'
        self.title_field = lambda index: InputField(self.title_field_locator(index), self.path, f'Title field (index: {index})')
        self.description_field = lambda index: InputField(self.description_field_locator(index), self.path, f'Description field (index: {index})')

    # -------------------------------------------- ㉧ LOCATORS {dynamic} (def)-------------------------------------------
    # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ⚠️ NOT USING ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╮
    def _title_field(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

    def _description_field(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')
    # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ FOR EXAMPLE ONLY ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╯

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Exercise form]
    # ───────────────────────────────────────────────────────────────────┐
    @allure.step('▶ Fill [Exercise form]')
    def fill(
        self,
        title: str,
        description: str,
        index: int = 0
    ):
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
        self.title_field(index).check_name(name=self.TITLE_FIELD_NAME)

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
        self.description_field(index).check_name(name=self.DESCRIPTION_FIELD_NAME)

    # Value
    def check_description_field_value(self, index: int = 0, description: str = 'Exercise description'):
        """
        ✔ Check [Description field] value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description (default: 'Exercise description')
        """
        self.description_field(index).check_value(value=description)

#=======================================================================================================================
