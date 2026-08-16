"""
Create course page > [Form] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


#=======================================================================================================================
"""
Form:
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
    # [Form]
    # ─────────────────────────────────────────────────┐
    def fill_form(
            self,
            title: str | None = None,
            estimated_time: str | None = None,
            description: str | None = None,
            max_score: str | None = None,
            min_score: str | None = None
    ):
        """
        ▶ Fill [Form] fields

        - ▶ Fields - fill

        :param title: Title (optional)
        :param estimated_time: Estimated time (optional)
        :param description: Description (optional)
        :param max_score: Max score (optional)
        :param min_score: Min score (optional)
        """
        self.fill_title_field(title)
        self.fill_estimated_time_field(estimated_time)
        self.fill_description_field(description)
        self.fill_max_score_field(max_score)
        self.fill_min_score_field(min_score)
    # ─────────────────────────────────────────────────┘
    # [Title field]
    def fill_title_field(self, title: str | None = None):
        """
        ▶ Fill [Title field]

        :param title: Title (optional)
        """
        if title is not None:
            self.title_field.fill(title)

    # [Estimated time field]
    def fill_estimated_time_field(self, estimated_time: str | None = None):
        """
        ▶ Fill [Estimated time field]

        :param estimated_time: Estimated time (optional)
        """
        if estimated_time is not None:
            self.estimated_time_field.fill(estimated_time)

    # [Description field]
    def fill_description_field(self, description: str | None = None):
        """
        ▶ Fill [Description field]

        :param description: Description (optional)
        """
        if description is not None:
            self.description_field.fill(description)

    # [Max score field]
    def fill_max_score_field(self, max_score: str | None = None):
        """
        ▶ Fill [Max score field]

        :param max_score: Max score (optional)
        """
        if max_score is not None:
            self.max_score_field.fill(max_score)

    # [Min score field]
    def fill_min_score_field(self, min_score: str | None = None):
        """
        ▶ Fill [Min score field]

        :param min_score: Min score (optional)
        """
        if min_score is not None:
            self.min_score_field.fill(min_score)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Form]
    # ────────────────────────────────────────────────┐
    def check_form(
            self,
            title: str | None = None,
            estimated_time: str | None = None,
            description: str | None = None,
            max_score: str | None = None,
            min_score: str | None = None):
        """
        ✔ Check [Course Form]

        If is passed:
        -------------
        - ✔ Fields - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Fields - visible
        - ✔ Field names - correct
        - ✔ Field placeholders/values - correct

        :param title: Title
        :param estimated_time: Estimated Time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        self.check_title_field(title)
        self.check_estimated_time_field(estimated_time)
        self.check_description_field(description)
        self.check_max_score_field(max_score)
        self.check_min_score_field(min_score)
    # ─────────────────────────────────────────────────┘

    # [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title_field(self, title: str | None = None):
        """
        ✔ Check [Title field]

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct

        :param title: Title (optional)
        """
        if title is not None:
            self.check_title_field_filled(title)
        else:
            self.check_title_field_visible()
            self.check_title_field_name()
            self.check_title_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_field_visible(self):
        """
        ✔ Check [Title field] visible

        .
        """
        error = f'❌ Create course page > Form > [Title field] - invisible!'
        expect(self.title_field, error).to_be_visible()

    def check_title_field_name(self):
        """
        ✔ Check [Title field] name

        .
        """
        error = f'❌ Create course page > Form > [Title field] - incorrect name!'
        expect(self.title_field, error).to_have_accessible_name(self.TITLE_FIELD_NAME)

    def check_title_field_placeholder(self):
        """
        ✔ Check [Title field] placeholder

        .
        """
        error = f'❌ Create course page > Form > [Title field] - incorrect placeholder!'
        expect(self.title_field, error).to_have_attribute('placeholder', self.TITLE_FIELD_PLACEHOLDER)

    def check_title_field_filled(self, title: str):
        """
        ✔ Check [Title field] filled correctly

        - ✔ Field - filled correctly

        :param title: Title
        """
        error = f'❌ Create course page > Form > [Title field] - filled incorrectly!'
        expect(self.title_field, error).to_have_value(title)


    # [Estimated time field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_estimated_time_field(self, estimated_time: str | None = None):
        """
        ✔ Check [Estimated time field]

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct

        :param estimated_time: Estimated time (optional)
        """
        if estimated_time is not None:
            self.check_estimated_time_field_filled(estimated_time)
        else:
            self.check_estimated_time_field_visible()
            self.check_estimated_time_field_name()
            self.check_estimated_time_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_estimated_time_field_visible(self):
        """
        ✔ Check [Estimated time field] visible

        .
        """
        error = f'❌ Create course page > Form > [Estimated time field] - invisible!'
        expect(self.estimated_time_field, error).to_be_visible()

    def check_estimated_time_field_name(self):
        """
        ✔ Check [Estimated time field] name

        .
        """
        error = f'❌ Create course page > Form > [Estimated time field] - incorrect name!'
        expect(self.estimated_time_field, error).to_have_accessible_name(self.ESTIMATED_TIME_FIELD_NAME)

    def check_estimated_time_field_placeholder(self):
        """
        ✔ Check [Estimated time field] placeholder

        .
        """
        error = f'❌ Create course page > Form > [Estimated time field] - incorrect placeholder!'
        expect(self.estimated_time_field, error).to_have_attribute('placeholder', self.ESTIMATED_TIME_FIELD_PLACEHOLDER)

    def check_estimated_time_field_filled(self, estimated_time: str):
        """
        ✔ Check [Estimated time field] filled correctly

        :param estimated_time: Estimated time
        """
        error = f'❌ Create course page > Form > [Estimated time field] - filled incorrectly!'
        expect(self.estimated_time_field, error).to_have_value(estimated_time)


    # [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_description_field(self, description: str | None = None):
        """
        ✔ Check [Description field]

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct

        :param description: Description (optional)
        """
        if description is not None:   # If is passed
            self.check_description_field_filled(description)
        else:
            self.check_description_field_visible()
            self.check_description_field_name()
            self.check_description_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_description_field_visible(self):
        """
        ✔ Check [Description field] visible

        .
        """
        error = f'❌ Create course page > Form > [Description field] - invisible!'
        expect(self.description_field, error).to_be_visible()

    def check_description_field_name(self):
        """
        ✔ Check [Description field] name correct

        .
        """
        error = f'❌ Create course page > Form > [Description field] - incorrect name!'
        expect(self.description_field, error).to_have_accessible_name(self.DESCRIPTION_FIELD_NAME)

    def check_description_field_placeholder(self):
        """
        ✔ Check [Description field] placeholder

        .
        """
        error = f'❌ Create course page > Form > [Description field] - incorrect placeholder!'
        expect(self.description_field, error).to_have_attribute('placeholder', self.DESCRIPTION_FIELD_PLACEHOLDER)

    def check_description_field_filled(self, description: str):
        """
        ✔ Check [Description field] filled correctly

        :param description: Description
        """
        error = f'❌ Create course page > Form > [Description field] - filled incorrectly!'
        expect(self.description_field, error).to_have_value(description)


    # [Max score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_max_score_field(self, max_score: str | None = None):
        """
        ✔ Check [Max score field]

         If is passed:
        --------------
        - ✔ Field - filled correctly

         If is NOT passed:
        ------------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - has a default value

        :param max_score: Max score (optional)
        """
        if max_score is not None:
            self.check_max_score_field_filled(max_score)
        else:
            self.check_max_score_field_visible()
            self.check_max_score_field_name()
            self.check_max_score_field_filled()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_max_score_field_visible(self):
        """
        ✔ Check [Max score field] visible

        .
        """
        error = f'❌ Create course page > Form > [Max score field] - invisible!'
        expect(self.max_score_field, error).to_be_visible()

    def check_max_score_field_name(self):
        """
        ✔ Check [Max score field] name

        .
        """
        error = f'❌ Create course page > Form > [Max score field] - incorrect name!'
        expect(self.max_score_field, error).to_have_accessible_name(self.MAX_SCORE_FIELD_NAME)

    def check_max_score_field_filled(self, max_score: str = '0'):
        """
        ✔ Check [Max score field] filled correctly

        :param max_score: Max score
        """
        error = f'❌ Create course page > Form > [Max score field] - filled incorrectly!'
        expect(self.max_score_field, error).to_have_value(max_score)


    # [Min score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_min_score_field(self, min_score: str | None = None):
        """
        ✔ Check [Min score field]

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - has a default value

        :param min_score: Min score (optional)
        """
        if min_score is not None:
            self.check_min_score_field_filled(min_score)
        else:
            self.check_min_score_field_visible()
            self.check_min_score_field_name()
            self.check_min_score_field_filled()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_min_score_field_visible(self):
        """
        ✔ Check [Min score field] visible

        .
        """
        error = f'❌ Create course page > Form > [Min score field] - invisible!'
        expect(self.min_score_field, error).to_be_visible()

    def check_min_score_field_name(self):
        """
        ✔ Check [Min score field] name

        .
        """
        error = f'❌ Create course page > Form > [Min score field] - incorrect name!'
        expect(self.min_score_field, error).to_have_accessible_name(self.MIN_SCORE_FIELD_NAME)

    def check_min_score_field_filled(self, min_score: str = '0'):
        """
        ✔ Check [Min score field] filled correctly

        :param min_score: Min score
        """
        error = f'❌ Create course page > Form > [Min score field] - filled incorrectly!'
        expect(self.min_score_field, error).to_have_value(min_score)


#=======================================================================================================================
