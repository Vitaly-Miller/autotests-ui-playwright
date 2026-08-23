"""
Create course page > [Form] (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
[Form]:
- Title field
- Estimated time field
- Description field
- Max score field
- Min score field
"""
class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # [Title]
        self.TITLE_FIELD_NAME = 'Title'
        self.TITLE_FIELD_PLACEHOLDER = 'New course'
        # [Estimated time]
        self.ESTIMATED_TIME_FIELD_NAME = 'Estimated time'
        self.ESTIMATED_TIME_FIELD_PLACEHOLDER = '1h 20m'
        # [Description]
        self.DESCRIPTION_FIELD_NAME = 'Description'
        self.DESCRIPTION_FIELD_PLACEHOLDER = 'Add description for course'
        # [Max score]
        self.MAX_SCORE_FIELD_NAME = 'Max score'
        # [Min score]
        self.MIN_SCORE_FIELD_NAME = 'Min score'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.title_field = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time_field = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.description_field = page.get_by_test_id('create-course-form-description-input').locator('textarea:visible') # ⚠
        self.max_score_field = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_field = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Course form]
    # ─────────────────────────────────────────────────┐
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

        - ▶ Fields -  ▶ fill | ✔ value

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
    # ─────────────────────────────────────────────────┘
    # [Title field]
    @allure.step('▶ Fill [Title field]')
    def fill_title_field(self, title: str):
        """
        ▶ Fill [Title field]

        - ▶ Field - fill
        - ✔ Field - value

        :param title: Title
        """
        self.title_field.fill(title)
        self.check_title_field_value(title)

    # [Estimated time field]
    @allure.step('▶ Fill [Estimated time field]')
    def fill_estimated_time_field(self, estimated_time: str):
        """
        ▶ Fill [Estimated time field]

        - ▶ Field - fill
        - ✔ Field - value

        :param estimated_time: Estimated time
        """
        self.estimated_time_field.fill(estimated_time)
        self.check_estimated_time_field_value(estimated_time)

    # [Description field]
    @allure.step('▶ Fill [Description field]')
    def fill_description_field(self, description: str):
        """
        ▶ Fill [Description field]

        - ▶ Field - fill
        - ✔ Field - value

        :param description: Description
        """
        self.description_field.fill(description)
        self.check_description_field_value(description)

    # [Max score field]
    @allure.step('▶ Fill [Max score field]')
    def fill_max_score_field(self, max_score: str):
        """
        ▶ Fill [Max score field]

        - ▶ Field - fill
        - ✔ Field - value

        :param max_score: Max score
        """
        self.max_score_field.fill(max_score)
        self.check_max_score_field_value(max_score)

    # [Min score field]
    @allure.step('▶ Fill [Min score field]')
    def fill_min_score_field(self, min_score: str):
        """
        ▶ Fill [Min score field]

        - ▶ Field - fill
        - ✔ Field - value

        :param min_score: Min score
        """
        self.min_score_field.fill(min_score)
        self.check_min_score_field_value(min_score)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Course form]
    # ────────────────────────────────────────────────┐
    def check_course_form(
            self,
            title: str | None = None,
            estimated_time: str | None = None,
            description: str | None = None,
            max_score: str | None = None,
            min_score: str | None = None
    ):
        """
        ✔ Check [Course form]

        If is passed:
        -------------
        - ✔ Fields - values

        If is NOT passed:
        ----------------
        - ✔ Fields - visible
        - ✔ Fields - names
        - ✔ Fields - placeholders / default values

        :param title: Title
        :param estimated_time: Estimated Time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        with allure.step(
                '✔ Check [Course form] field values'
                if all(param is not None for param in (title, estimated_time, description, max_score, min_score))
                else '✔ Check [Course form] UI'
        ):
            self.check_title_field(title)
            self.check_estimated_time_field(estimated_time)
            self.check_description_field(description)
            self.check_max_score_field(max_score)
            self.check_min_score_field(min_score)
    # ─────────────────────────────────────────────────┘

    # [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
            with allure.step('✔ Check [Title field] value'):
                self.check_title_field_value(title)
        else:
            with allure.step('✔ Check [Title field] UI'):
                self.check_title_field_visible()
                self.check_title_field_name()
                self.check_title_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Title field] visible')
    def check_title_field_visible(self):
        """
        ✔ Check [Title field] visible

        .
        """
        error = f'❌ Create course page > Form > [Title field] - invisible!'
        expect(self.title_field, error).to_be_visible()

    @allure.step('✔ Check [Title field] name')
    def check_title_field_name(self):
        """
        ✔ Check [Title field] name

        .
        """
        error = f'❌ Create course page > Form > [Title field] - incorrect name!'
        expect(self.title_field, error).to_have_accessible_name(self.TITLE_FIELD_NAME)

    @allure.step('✔ Check [Title field] placeholder')
    def check_title_field_placeholder(self):
        """
        ✔ Check [Title field] placeholder

        .
        """
        error = f'❌ Create course page > Form > [Title field] - incorrect placeholder!'
        expect(self.title_field, error).to_have_attribute('placeholder', self.TITLE_FIELD_PLACEHOLDER)

    @allure.step('✔ Check [Title field] value')
    def check_title_field_value(self, title: str):
        """
        ✔ Check [Title field] value

        - ✔ Field - value

        :param title: Title
        """
        error = f'❌ Create course page > Form > [Title field] - incorrect value!'
        expect(self.title_field, error).to_have_value(title)


    # [Estimated time field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
            with allure.step('✔ Check [Estimated time field] value'):
                self.check_estimated_time_field_value(estimated_time)
        else:
            with allure.step('✔ Check [Estimated time field] UI'):
                self.check_estimated_time_field_visible()
                self.check_estimated_time_field_name()
                self.check_estimated_time_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Estimated time field] visible')
    def check_estimated_time_field_visible(self):
        """
        ✔ Check [Estimated time field] visible

        .
        """
        error = f'❌ Create course page > Form > [Estimated time field] - invisible!'
        expect(self.estimated_time_field, error).to_be_visible()

    @allure.step('✔ Check [Estimated time field] name')
    def check_estimated_time_field_name(self):
        """
        ✔ Check [Estimated time field] name

        .
        """
        error = f'❌ Create course page > Form > [Estimated time field] - incorrect name!'
        expect(self.estimated_time_field, error).to_have_accessible_name(self.ESTIMATED_TIME_FIELD_NAME)

    @allure.step('✔ Check [Estimated time field] placeholder')
    def check_estimated_time_field_placeholder(self):
        """
        ✔ Check [Estimated time field] placeholder

        .
        """
        error = f'❌ Create course page > Form > [Estimated time field] - incorrect placeholder!'
        expect(self.estimated_time_field, error).to_have_attribute('placeholder', self.ESTIMATED_TIME_FIELD_PLACEHOLDER)

    @allure.step('✔ Check [Estimated time field] value')
    def check_estimated_time_field_value(self, estimated_time: str):
        """
        ✔ Check [Estimated time field] value

        :param estimated_time: Estimated time
        """
        error = f'❌ Create course page > Form > [Estimated time field] - incorrect value!'
        expect(self.estimated_time_field, error).to_have_value(estimated_time)


    # [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
            with allure.step('✔ Check [Description field] value'):
                self.check_description_field_value(description)
        else:
            with allure.step('✔ Check [Description field] UI'):
                self.check_description_field_visible()
                self.check_description_field_name()
                self.check_description_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Description field] visible')
    def check_description_field_visible(self):
        """
        ✔ Check [Description field] visible

        .
        """
        error = f'❌ Create course page > Form > [Description field] - invisible!'
        expect(self.description_field, error).to_be_visible()

    @allure.step('✔ Check [Description field] name')
    def check_description_field_name(self):
        """
        ✔ Check [Description field] name correct

        .
        """
        error = f'❌ Create course page > Form > [Description field] - incorrect name!'
        expect(self.description_field, error).to_have_accessible_name(self.DESCRIPTION_FIELD_NAME)

    @allure.step('✔ Check [Description field] placeholder')
    def check_description_field_placeholder(self):
        """
        ✔ Check [Description field] placeholder

        .
        """
        error = f'❌ Create course page > Form > [Description field] - incorrect placeholder!'
        expect(self.description_field, error).to_have_attribute('placeholder', self.DESCRIPTION_FIELD_PLACEHOLDER)

    @allure.step('✔ Check [Description field] description')
    def check_description_field_value(self, description: str):
        """
        ✔ Check [Description field] value

        :param description: Description
        """
        error = f'❌ Create course page > Form > [Description field] - incorrect value!'
        expect(self.description_field, error).to_have_value(description)


    # [Max score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_max_score_field(self, max_score: str | None = None):
        """
        ✔ Check [Max score field]

         If is passed:
        --------------
        - ✔ Field - value

         If is NOT passed:
        ------------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param max_score: Max score (optional)
        """
        if max_score is not None:
            with allure.step('✔ Check [Max score field] value'):
                self.check_max_score_field_value(max_score)
        else:
            with allure.step('✔ Check [Max score field] UI'):
                self.check_max_score_field_visible()
                self.check_max_score_field_name()
                self.check_max_score_field_value()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Max score field] visible')
    def check_max_score_field_visible(self):
        """
        ✔ Check [Max score field] visible

        .
        """
        error = f'❌ Create course page > Form > [Max score field] - invisible!'
        expect(self.max_score_field, error).to_be_visible()

    @allure.step('✔ Check [Max score field] name')
    def check_max_score_field_name(self):
        """
        ✔ Check [Max score field] name

        .
        """
        error = f'❌ Create course page > Form > [Max score field] - incorrect name!'
        expect(self.max_score_field, error).to_have_accessible_name(self.MAX_SCORE_FIELD_NAME)

    @allure.step('✔ Check [Max score field] value')
    def check_max_score_field_value(self, max_score: str = '0'):
        """
        ✔ Check [Max score field] value

        :param max_score: Max score
        """
        error = f'❌ Create course page > Form > [Max score field] - incorrect value!'
        expect(self.max_score_field, error).to_have_value(max_score)


    # [Min score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
            with allure.step('✔ Check [Min score field] value'):
                self.check_min_score_field_value(min_score)
        else:
            with allure.step('✔ Check [Min score field] UI'):
                self.check_min_score_field_visible()
                self.check_min_score_field_name()
                self.check_min_score_field_value()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Min score field] visible')
    def check_min_score_field_visible(self):
        """
        ✔ Check [Min score field] visible

        .
        """
        error = f'❌ Create course page > Form > [Min score field] - invisible!'
        expect(self.min_score_field, error).to_be_visible()

    @allure.step('✔ Check [Min score field] name')
    def check_min_score_field_name(self):
        """
        ✔ Check [Min score field] name

        .
        """
        error = f'❌ Create course page > Form > [Min score field] - incorrect name!'
        expect(self.min_score_field, error).to_have_accessible_name(self.MIN_SCORE_FIELD_NAME)

    @allure.step('✔ Check [Min score field] value')
    def check_min_score_field_value(self, min_score: str = '0'):
        """
        ✔ Check [Min score field] value

        :param min_score: Min score
        """
        error = f'❌ Create course page > Form > [Min score field] - incorrect value!'
        expect(self.min_score_field, error).to_have_value(min_score)


#=======================================================================================================================
