"""
Create course page > Exercises > Exercise > [Form] (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page, expect

#=======================================================================================================================
"""
[Form]:
- Title field
- Description field
"""
class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # Fields names
        self.TITLE_FIELD_NAME = 'Title'
        self.DESCRIPTION_FIELD_NAME = 'Description'

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.form_component = '❌ Create course page > Exercises > Exercise > Form'
        self.title_field_element = lambda index: f'{self.form_component} > [Title] (index: {index})'
        self.description_field_element = lambda index: f'{self.form_component} > [Description field] (index: {index})'

        # --------------------------------------- ㉧ LOCATORS {dynamic} (lambda) ----------------------------------------
        self.title_field = lambda index: page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        self.description_field = lambda index: page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')

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

        - ▶ Title field - fill
        - ▶ Description field - fill

        :param title: Title
        :param description: Description
        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.fill_title_field(index=index, title=title)
        self.fill_description_field(index=index, description=description)
    # ───────────────────────────────────────────────────────────────────┘
    # Fill [Title field]
    @allure.step('▶ Fill [Title field]')
    def fill_title_field(self, title: str, index: int = 0):
        """
        ▶ Fill [Title field]

        - ▶ Field - fill
        - ✔ Field - value

        :param title: Title
        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.title_field(index).fill(title)
        self.check_title_field_value(index, title)

    # Fill [Description field]
    @allure.step('▶ Fill [Description field]')
    def fill_description_field(self, description: str, index: int = 0):
        """
        ▶ Fill [Description field]

        - ▶ Field - fill
        - ✔ Field - value

        :param description: Description
        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.description_field(index).fill(description)
        self.check_description_field_value(index, description)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Exercise form]
    # ────────────────────────────────────────────────────────────────────────┐
    def check(
            self,
            index: int = 0,
            title: str | None = None,
            description: str | None = None
    ):
        """
        ✔ Check [Exercise form]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        :param description: Exercise description
        """
        with allure.step(
            '✔ Check [Exercise form] field values'
            if all(param is not None for param in (title, description))
            else '✔ Check [Exercise form] UI'
        ):
            self.check_title_field(index=index, title=title)
            self.check_description_field(index=index, description=description)
    # ────────────────────────────────────────────────────────────────────────┘

    # [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
        :param title: Title
        """
        if title is not None:
            with allure.step('✔ Check [Title field] value'):
                self.check_title_field_value(index=index, title=title)
        else:
            with allure.step('✔ Check [Title field] UI'):
                self.check_title_field_visible(index)
                self.check_title_field_name(index)
                self.check_title_field_value(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Title field] is visible')
    def check_title_field_visible(self, index: int = 0):
        """
        ✔ Check [Title field]  is visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'{self.title_field_element(index)} - invisible!'
        expect(self.title_field(index), error).to_be_visible()

    @allure.step('✔ Check [Title field] name')
    def check_title_field_name(self, index: int = 0):
        """
        ✔ Check [Title field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'{self.title_field_element(index)} - incorrect name!'
        expect(self.title_field(index), error).to_have_accessible_name(self.TITLE_FIELD_NAME)

    @allure.step('✔ Check [Title field] value')
    def check_title_field_value(self, index: int = 0, title: str = 'Exercise title'):
        """
        ✔ Check [Title field] value

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        """
        error = f'{self.title_field_element(index)} - incorrect value!'
        expect(self.description_field(index), error).to_have_value(title)


    # [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
        :param description: Description
        """
        if description is not None:
            with allure.step('✔ Check [Description field] value'):
                self.check_description_field_value(index=index, description=description)
        else:
            with allure.step('✔ Check [Description field] UI'):
                self.check_description_field_visible(index)
                self.check_description_field_name(index)
                self.check_description_field_value(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Description field] is visible')
    def check_description_field_visible(self, index: int = 0):
        """
        ✔ Check [Description field]  is visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'{self.description_field_element(index)} - invisible!'
        expect(self.description_field(index), error).to_be_visible()

    @allure.step('✔ Check [Description field] name')
    def check_description_field_name(self, index: int = 0):
        """
        ✔ Check [Description field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'{self.description_field_element(index)} - incorrect name!'
        expect(self.description_field(index), error).to_have_accessible_name(self.DESCRIPTION_FIELD_NAME)

    @allure.step('✔ Check [Description field] value')
    def check_description_field_value(self, index: int = 0, description: str = 'Exercise description'):
        """
        ✔ Check [Description field] value

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description
        """
        error = f'{self.description_field_element(index)} - incorrect value!'
        expect(self.description_field(index), error).to_have_value(description)


#=======================================================================================================================
