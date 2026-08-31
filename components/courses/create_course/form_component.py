"""
Create course page > [Form]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.input_field import InputField

#=======================================================================================================================
"""
[Form]:
- Title input field
- Estimated time input field
- Description input field
- Max score input field
- Min score input field
"""
class CreateCourseFormComponent(BaseComponent):
    path = 'Create course page > Form'

    # 𝌆 DATA
    TITLE_FIELD_NAME = 'Title'
    TITLE_FIELD_PLACEHOLDER = 'New course'
    ESTIMATED_TIME_FIELD_NAME = 'Estimated time'
    ESTIMATED_TIME_FIELD_PLACEHOLDER = '1h 20m'
    DESCRIPTION_FIELD_NAME = 'Description'
    DESCRIPTION_FIELD_PLACEHOLDER = 'Add description for course'
    MAX_SCORE_FIELD_NAME = 'Max score'
    MAX_SCORE_FIELD_DEFAULT_VALUE = '0'
    MIN_SCORE_FIELD_NAME = 'Min score'
    MIN_SCORE_FIELD_DEFAULT_VALUE = '0'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-title-input').locator('input')

    def estimated_time_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-estimated-time-input').locator('input')

    def description_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-description-input').locator('textarea:visible')  # ⚠

    def max_score_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-max-score-input').locator('input')

    def min_score_field_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-form-min-score-input').locator('input')

    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title_field(self) -> InputField:
        return InputField(self.title_field_locator(), self.path, 'Title field')

    def estimated_time_field(self) -> InputField:
        return InputField(self.estimated_time_field_locator(), self.path, 'Estimated time field')

    def description_field(self) -> InputField:
        return InputField(self.description_field_locator(), self.path, 'Description field')

    def max_score_field(self) -> InputField:
        return InputField(self.max_score_field_locator(), self.path, 'Max score field')

    def min_score_field(self) -> InputField:
        return InputField(self.min_score_field_locator(), self.path, 'Min score field')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Course form]
    # ────────────────────────────────────┐
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

        - Title field - ▶ fill | ✔ value
        - Estimated time field - ▶ fill | ✔ value
        - Description field - ▶ fill | ✔ value
        - Max score field - ▶ fill | ✔ value
        - Min score field - ▶ fill | ✔ value

        :param title: Title
        :param estimated_time: Estimated time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        self.fill_title_field(title)
        self.fill_estimated_time_field(estimated_time)
        self.fill_description_field(description)
        self.fill_max_score_field(max_score)
        self.fill_min_score_field(min_score)
    # ────────────────────────────────────┘
    # Fill [Title field]
    def fill_title_field(self, title: str):
        """
        ▶ Fill [Title field]

        :param title: Title
        """
        self.title_field().fill(title)

    # Fill [Estimated time field]
    def fill_estimated_time_field(self, estimated_time: str):
        """
        ▶ Fill [Estimated time field]

        :param estimated_time: Estimated time
        """
        self.estimated_time_field().fill(estimated_time)

    # Fill [Description field]
    def fill_description_field(self, description: str):
        """
        ▶ Fill [Description field]

        :param description: Description
        """
        self.description_field().fill(description)

    # Fill [Max score field]
    def fill_max_score_field(self, max_score: str):
        """
        ▶ Fill [Max score field]

        :param max_score: Max score
        """
        self.max_score_field().fill(max_score)

    # Fill [Min score field]
    def fill_min_score_field(self, min_score: str):
        """
        ▶ Fill [Min score field]

        :param min_score: Min score
        """
        self.min_score_field().fill(min_score)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Course Form]
    # ─────────────────────────────────────┐
    @allure.step('✔ Check [Course form]')
    def check(
        self,
        title: str | None = None,
        estimated_time: str | None = None,
        description: str | None = None,
        max_score: str | None = None,
        min_score: str | None = None
    ):
        """
        ✔ Check [Course form]

        - ✔ Title field - value / UI
        - ✔ Estimated time field - value / UI
        - ✔ Description field - value / UI
        - ✔ Max score field - value / UI
        - ✔ Min score field - value / UI

        :param title: Title (optional)
        :param estimated_time: Estimated time (optional)
        :param description: Description (optional)
        :param max_score: Max score (optional)
        :param min_score: Min score (optional)
        """
        self.check_title_field(title)
        self.check_estimated_time_field(estimated_time)
        self.check_description_field(description)
        self.check_max_score_field(max_score)
        self.check_min_score_field(min_score)
    # ─────────────────────────────────────┘

    # [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title field]')
    def check_title_field(self, title: str | None = None):
        """
        ✔ Check [Title field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - placeholder

        :param title: Title (optional)
        """
        if title is not None:
            self.check_title_field_value(title)
        else:
            self.check_title_field_visible()
            self.check_title_field_name()
            self.check_title_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_title_field_visible(self):
        """
        ✔ Check [Title field] is visible

        .
        """
        self.title_field().check_visible()

    # Name
    def check_title_field_name(self):
        """
        ✔ Check [Title field] name

        .
        """
        self.title_field().check_name(name=self.TITLE_FIELD_NAME)

    # Placeholder
    def check_title_field_placeholder(self):
        """
        ✔ Check [Title field] placeholder

        .
        """
        self.title_field().check_placeholder(placeholder=self.TITLE_FIELD_PLACEHOLDER)

    # Value
    def check_title_field_value(self, title: str):
        """
        ✔ Check [Title field] value

        :param title: Title
        """
        self.title_field().check_value(value=title)


    # [Estimated time field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Estimated time field]')
    def check_estimated_time_field(self, estimated_time: str | None = None):
        """
        ✔ Check [Estimated time field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - placeholder

        :param estimated_time: Estimated time (optional)
        """
        if estimated_time is not None:
            self.check_estimated_time_field_value(estimated_time)
        else:
            self.check_estimated_time_field_visible()
            self.check_estimated_time_field_name()
            self.check_estimated_time_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_estimated_time_field_visible(self):
        """
        ✔ Check [Estimated time field] is visible

        .
        """
        self.estimated_time_field().check_visible()

    # Name
    def check_estimated_time_field_name(self):
        """
        ✔ Check [Estimated time field] name

        .
        """
        self.estimated_time_field().check_name(name=self.ESTIMATED_TIME_FIELD_NAME)

    # Placeholder
    def check_estimated_time_field_placeholder(self):
        """
        ✔ Check [Estimated time field] placeholder

        .
        """
        self.estimated_time_field().check_placeholder(placeholder=self.ESTIMATED_TIME_FIELD_PLACEHOLDER)

    # Value
    def check_estimated_time_field_value(self, estimated_time: str):
        """
        ✔ Check [Estimated time field] value

        :param estimated_time: Estimated time
        """
        self.estimated_time_field().check_value(value=estimated_time)


    # [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Description field]')
    def check_description_field(self, description: str | None = None):
        """
        ✔ Check [Description field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - placeholder

        :param description: Description (optional)
        """
        if description is not None:
            self.check_description_field_value(description)
        else:
            self.check_description_field_visible()
            self.check_description_field_name()
            self.check_description_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_description_field_visible(self):
        """
        ✔ Check [Description field] is visible

        .
        """
        self.description_field().check_visible()

    # Name
    def check_description_field_name(self):
        """
        ✔ Check [Description field] name

        .
        """
        self.description_field().check_name(name=self.DESCRIPTION_FIELD_NAME)

    # Placeholder
    def check_description_field_placeholder(self):
        """
        ✔ Check [Description field] placeholder

        .
        """
        self.description_field().check_placeholder(placeholder=self.DESCRIPTION_FIELD_PLACEHOLDER)

    # Value
    def check_description_field_value(self, description: str):
        """
        ✔ Check [Description field] value

        :param description: Description
        """
        self.description_field().check_value(value=description)


    # [Max score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Max score field]')
    def check_max_score_field(self, max_score: str | None = None):
        """
        ✔ Check [Max score field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param max_score: Max score (optional)
        """
        if max_score is not None:
            self.check_max_score_field_value(max_score)
        else:
            self.check_max_score_field_visible()
            self.check_max_score_field_name()
            self.check_max_score_field_value()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_max_score_field_visible(self):
        """
        ✔ Check [Max score field] is visible

        .
        """
        self.max_score_field().check_visible()

    # Name
    def check_max_score_field_name(self):
        """
        ✔ Check [Max score field] name

        .
        """
        self.max_score_field().check_name(name=self.MAX_SCORE_FIELD_NAME)

    # Value
    def check_max_score_field_value(self, max_score: str = MAX_SCORE_FIELD_DEFAULT_VALUE):
        """
        ✔ Check [Max score field] value

        :param max_score: Max score (default: '0')
        """
        self.max_score_field().check_value(value=max_score)


    # [Min score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Min score field]')
    def check_min_score_field(self, min_score: str | None = None):
        """
        ✔ Check [Min score field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param min_score: Min score (optional)
        """
        if min_score is not None:
            self.check_min_score_field_value(min_score)
        else:
            self.check_min_score_field_visible()
            self.check_min_score_field_name()
            self.check_min_score_field_value()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_min_score_field_visible(self):
        """
        ✔ Check [Min score field] is visible

        .
        """
        self.min_score_field().check_visible()

    # Name
    def check_min_score_field_name(self):
        """
        ✔ Check [Min score field] name

        .
        """
        self.min_score_field().check_name(name=self.MIN_SCORE_FIELD_NAME)

    # Value
    def check_min_score_field_value(self, min_score: str = MAX_SCORE_FIELD_DEFAULT_VALUE):
        """
        ✔ Check [Min score field] value

        :param min_score: Min score (default: '0')
        """
        self.min_score_field().check_value(value=min_score)


#=======================================================================================================================
