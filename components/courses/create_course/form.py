"""
Create course form (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.input_field import InputField

#=======================================================================================================================
class CreateCourseFormComponent(BaseComponent):
    """
    Create course form (component)

    - Title input field
    - Estimated time input field
    - Description input field
    - Max score input field
    - Min score input field
    """
    PATH = 'Create course page > Form'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-title-input').locator('input')

    def estimated_time_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-estimated-time-input').locator('input')

    def description_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-description-input').locator('textarea:visible')  # ⚠

    def max_score_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-max-score-input').locator('input')

    def min_score_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-min-score-input').locator('input')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title_input_field(self) -> InputField:
        return InputField(self.title_input_field_locator(), self.PATH, 'Title input field')

    def estimated_time_input_field(self) -> InputField:
        return InputField(self.estimated_time_input_field_locator(), self.PATH, 'Estimated time input field')

    def description_input_field(self) -> InputField:
        return InputField(self.description_input_field_locator(), self.PATH, 'Description input field')

    def max_score_input_field(self) -> InputField:
        return InputField(self.max_score_input_field_locator(), self.PATH, 'Max score input field')

    def min_score_input_field(self) -> InputField:
        return InputField(self.min_score_input_field_locator(), self.PATH, 'Min score input field')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Course form]
    # ─────────────────────────────────────────────────────────┐
    @allure.step('▶ Fill [Course form]')
    def fill(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str
    ):
        """
        ▶ Fill [Course form]

        - Title input field - ▶ fill | ✔ value
        - Estimated time input field - ▶ fill | ✔ value
        - Description input field - ▶ fill | ✔ value
        - Max score input field - ▶ fill | ✔ value
        - Min score input field - ▶ fill | ✔ value

        :param title: Title
        :param estimated_time: Estimated time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        self.fill_title_input_field(title)
        self.fill_estimated_time_input_field(estimated_time)
        self.fill_description_input_field(description)
        self.fill_max_score_input_field(max_score)
        self.fill_min_score_input_field(min_score)
    # ─────────────────────────────────────────────────────────┘
    # Fill [Title input field]
    def fill_title_input_field(self, title: str):
        """
        ▶ Fill [Title input field]

        :param title: Title
        """
        self.title_input_field().fill(title)

    # Fill [Estimated time input field]
    def fill_estimated_time_input_field(self, estimated_time: str):
        """
        ▶ Fill [Estimated time input field]

        :param estimated_time: Estimated time
        """
        self.estimated_time_input_field().fill(estimated_time)

    # Fill [Description input field]
    def fill_description_input_field(self, description: str):
        """
        ▶ Fill [Description input field]

        :param description: Description
        """
        self.description_input_field().fill(description)

    # Fill [Max score input field]
    def fill_max_score_input_field(self, max_score: str):
        """
        ▶ Fill [Max score input field]

        :param max_score: Max score
        """
        self.max_score_input_field().fill(max_score)

    # Fill [Min score input field]
    def fill_min_score_input_field(self, min_score: str):
        """
        ▶ Fill [Min score input field]

        :param min_score: Min score
        """
        self.min_score_input_field().fill(min_score)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Course Form]
    # ─────────────────────────────────────┐
    @allure.step('✔ Check [Course form]')
    def check(
        self,
        title: str = '',
        estimated_time: str = '',
        description: str = '',
        max_score: str = '0',
        min_score: str = '0'
    ):
        """
        ✔ Check [Course form]

        - ✔ Title input field
        - ✔ Estimated time input field
        - ✔ Description input field
        - ✔ Max score input field
        - ✔ Min score input field

        :param title: Title (Empty by default)
        :param estimated_time: Estimated time (Empty by default)
        :param description: Description (Empty by default)
        :param max_score: Max score (Default: '0')
        :param min_score: Min score (Default: '0')
        """
        self.check_title_input_field(title)
        self.check_estimated_time_input_field(estimated_time)
        self.check_description_input_field(description)
        self.check_max_score_input_field(max_score)
        self.check_min_score_input_field(min_score)
    # ─────────────────────────────────────┘

    # [Title input field]
    @allure.step('✔ Check [Title input field]')
    def check_title_input_field(self, title: str = ''):
        """
        ✔ Check [Title input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - placeholder
        - ✔ Field - value (Empty by default)

        :param title: Title (optional)
        """
        self.title_input_field().check_visible()
        self.title_input_field().check_name(name='Title')
        self.title_input_field().check_placeholder(placeholder='New course')
        self.title_input_field().check_value(title)

    # [Estimated time input field]
    @allure.step('✔ Check [Estimated time input field]')
    def check_estimated_time_input_field(self, estimated_time: str = ''):
        """
        ✔ Check [Estimated time input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - placeholder
        - ✔ Field - value (Empty by default)

        :param estimated_time: Estimated time (optional)
        """
        self.estimated_time_input_field().check_visible()
        self.estimated_time_input_field().check_name(name='Estimated time')
        self.estimated_time_input_field().check_placeholder(placeholder='1h 20m')
        self.estimated_time_input_field().check_value(estimated_time)

    # [Description input field]
    @allure.step('✔ Check [Description input field]')
    def check_description_input_field(self, description: str = ''):
        """
        ✔ Check [Description input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - placeholder
        - ✔ Field - value (Empty by default)

        :param description: Description (optional)
        """
        self.description_input_field().check_visible()
        self.description_input_field().check_name(name='Description')
        self.description_input_field().check_placeholder(placeholder='Add description for course')
        self.description_input_field().check_value(description)

    # [Max score input field]
    @allure.step('✔ Check [Max score input field]')
    def check_max_score_input_field(self, max_score: str = '0'):
        """
        ✔ Check [Max score input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - value (Default: '0')

        :param max_score: Max score (optional)
        """
        self.max_score_input_field().check_visible()
        self.max_score_input_field().check_name(name='Max score')
        self.max_score_input_field().check_value(max_score)

    # [Min score input field]
    @allure.step('✔ Check [Min score input field]')
    def check_min_score_input_field(self, min_score: str = '0'):
        """
        ✔ Check [Min score input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - value (Default: '0')

        :param min_score: Min score (optional)
        """
        self.min_score_input_field().check_visible()
        self.min_score_input_field().check_name(name='Min score')
        self.min_score_input_field().check_value(min_score)

#=======================================================================================================================
