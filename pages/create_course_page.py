"""
Create Course page
"""
from components.courses.create_course.exercise_component import CreateCourseExerciseComponent
from components.courses.create_course.exercises_toolbar_component import CreateCourseExercisesToolbarComponent
from components.courses.create_course.image_upload_widget_component import CreateCourseImageUploadWidgetComponent
from components.courses.create_course.toolbar_component import CreateCourseToolbarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.navigation.navbar.navbar_component import NavbarComponent
from components.navigation.sidebar.sidebar_component import SidebarComponent



#=======================================================================================================================
class CreateCoursePage(BasePage):        # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'

    def __init__(self, page: Page):      # Конструктор класса, принимающий Page
        super().__init__(page)           # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        # Page > [Toolbar]
        self.TOOLBAR_TITLE = 'Create course'

        # Course > [Form]
        self.TITLE_FIELD_NAME = 'Title'
        self.TITLE_FIELD_PLACEHOLDER = 'New course'
        self.ESTIMATED_TIME_FIELD_NAME = 'Estimated time'
        self.ESTIMATED_TIME_FIELD_PLACEHOLDER = '1h 20m'
        self.DESCRIPTION_FIELD_NAME = 'Description'
        self.DESCRIPTION_FIELD_PLACEHOLDER = 'Add description for course'
        self.MAX_SCORE_FIELD_NAME = 'Max score'
        self.MIN_SCORE_FIELD_NAME = 'Min score'


        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CreateCourseToolbarComponent(page)
        self.image_upload_widget = CreateCourseImageUploadWidgetComponent(page)
        self.exercises_toolbar = CreateCourseExercisesToolbarComponent(page)
        self.exercise = CreateCourseExerciseComponent(page)


        # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------

        # Course Form
        self.course_form_title_field = page.get_by_role(role='textbox', name='Title')
        self.course_form_estimated_time_field = page.get_by_role(role='textbox', name='Estimated time')
        self.course_form_description_field = page.get_by_role(role='textbox', name='Description')
        self.course_form_max_score_field = page.get_by_role(role='spinbutton', name='Max score')
        self.course_form_min_score_field = page.get_by_role(role='spinbutton', name='Min score')


      # [Empty view]
        self.EXERCISES_IDENTIFIER = 'create-course-exercises'
        self.EXERCISES_EMPTY_VIEW_TITLE = 'There is no exercises'
        self.EXERCISES_EMPTY_VIEW_DESCRIPTION = 'Click on "Create exercise" button to create new exercise'

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str):
        """
        ▶ ▶ Fill Create course form of the Create course page

        - ▶ Form fields - fill
        - ✔ Form fields - filled correctly

        :param title: Title
        :param estimated_time: Estimated Time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        self.course_form_title_field.fill(title)
        self.course_form_estimated_time_field.fill(estimated_time)
        self.course_form_description_field.fill(description)
        self.course_form_max_score_field.fill(max_score)
        self.course_form_min_score_field.fill(min_score)
        self.check_course_form(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score)



    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar:
    # ─────────────────────────────────────────────────┐
    def check_toolbar(self):
        """
        ✔ Check <Courses Toolbar> of the Create course page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ <Create Course button> - visible
        - ✔ <Create Course button> - enable
        """
        self.check_toolbar_title_visible()
        self.check_toolbar_title_text()
        self.check_toolbar_create_course_btn_visible()
        self.check_toolbar_create_course_btn_disabled()
    # ─────────────────────────────────────────────────┘
    # Toolbar [Title]
    def check_toolbar_title_visible(self):
        """
        ✔ Check <Toolbar [Title]> of the Create course page - visible

        - ✔ Title - visible
        """
        error = f'❌ <Toolbar [Title]> of the Create course page - invisible!'
        expect(self.toolbar_title, error).to_be_visible()

    def check_toolbar_title_text(self):
        """
        ✔ Check <Toolbar [Title] text> of the Create course page

        did - correct
        """
        error = f'❌ <Toolbar [Title] text> of the Create course page - incorrect!'
        expect(self.toolbar_title, error).to_have_text(self.TOOLBAR_TITLE)

    # Toolbar [Create Course button]
    def check_toolbar_create_course_btn_visible(self):
        """
        ✔ Check <Toolbar [Create Course button]> of the Create course page - visible

        - ✔ Button - visible
        """
        error = f'❌ <Toolbar [Create Course button]> of the Create course page - invisible!'
        expect(self.create_course_btn, error).to_be_visible()

    def check_toolbar_create_course_btn_enabled(self):
        """
        ✔ Check <Toolbar [Create Course button]> of the Create course page - enabled

        - ✔ Button - enabled
        """
        error = f'❌ <Toolbar [Create Course button]> of the Create course page - disabled!'
        expect(self.create_course_btn, error).to_be_enabled()

    def check_toolbar_create_course_btn_disabled(self):
        """
        ✔ Check <Toolbar [Create Course button]> of the Create course page - disabled

        - ✔ Button - disabled
        """
        error = f'❌ <Toolbar [Create Course button]> of the Create course page - enabled!'
        expect(self.create_course_btn, error).to_be_disabled()


    # Course Form:
    # ────────────────────────────────────────────────────┐
    def check_course_form(
            self,
            title: str | None = None,
            estimated_time: str | None = None,
            description: str | None = None,
            max_score: str | None = None,
            min_score: str | None = None):
        """
        ✔ Check <Course Form> of the Create course page

        - ✔ Form fields - visible
        - ✔ Form fields - correct
        - ✔ Form field Placeholders - correct (Except: Max/Min-score fields)
        - ✔ Form fields - filled correctly (If is passed)

        :param title: Title
        :param estimated_time: Estimated Time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        self.check_course_title(title)
        self.check_course_estimated_time(estimated_time)
        self.check_course_description(description)
        self.check_course_max_score(max_score)
        self.check_course_min_score(min_score)
    # ────────────────────────────────────────────────────┘

    # Course Form [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_course_title(self, title: str | None = None):
        """
        ✔ Check <Course [Title field]> of the Create course page

        If filled:
        ----------
        - ✔ Field - filled correctly

        If did not fill:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct

        :param title: Title (optional)
        """
        if title:   # If is passed
            self.check_course_title_field_filled_correctly(title)
        else:
            self.check_course_title_field_visible()
            self.check_course_title_field_name()
            self.check_course_title_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_course_title_field_visible(self):
        """
        ✔ Check <Course [Title field]> of the Create course page - visible!

        - ✔ Title field - visible
        """
        error = f'❌ <Course [Title field]> of the Create course page - invisible!'
        expect(self.course_form_title_field, error).to_be_visible()

    def check_course_title_field_name(self):
        """
        ✔ Check <Course [Title field] name> of the Create course page - correct!

        - ✔ Title name - correct
        """
        error = f'❌ <Course [Title field] name> of the Create course page - incorrect!'
        expect(self.course_form_title_field, error).to_have_accessible_name(self.TITLE_FIELD_NAME)

    def check_course_title_field_placeholder(self):
        """
        ✔ Check <Course [Title field] Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct
        """
        error = f'❌ <Course [Title field] Placeholder> of the Create course page - incorrect!'
        expect(self.course_form_title_field, error).to_have_attribute('placeholder', self.TITLE_FIELD_PLACEHOLDER)

    def check_course_title_field_filled_correctly(self, title: str):
        """
        ✔ Check <Course [Title field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param title: Title
        """
        error = f'❌ <Course [Title field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_title_field, error).to_have_value(title)


    # Course Form [Estimated time field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_course_estimated_time(self, estimated_time: str | None = None):
        """
        ✔ Check <Course [Estimated time field]> of the Create course page

        If filled:
        ----------
        - ✔ Field - filled correctly

        If did not fill:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct

        :param estimated_time: Estimated time (optional)
        """
        if estimated_time:   # If is passed
            self.check_course_estimated_time_field_filled_correctly(estimated_time)
        else:
            self.check_course_estimated_time_field_visible()
            self.check_course_estimated_time_field_name()
            self.check_course_estimated_time_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_course_estimated_time_field_visible(self):
        """
        ✔ Check <Course [Estimated time field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = f'❌ <Course [Estimated time field]> of the Create course page - invisible!'
        expect(self.course_form_estimated_time_field, error).to_be_visible()

    def check_course_estimated_time_field_name(self):
        """
        ✔ Check <Course [Estimated time field] name> of the Create course page - correct!

        - ✔ Field name - correct
        """
        error = f'❌ <Course [Estimated time field] name> of the Create course page - incorrect!'
        expect(self.course_form_estimated_time_field, error).to_have_accessible_name(self.ESTIMATED_TIME_FIELD_NAME)

    def check_course_estimated_time_field_placeholder(self):
        """
        ✔ Check <Course [Estimated time field] Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct
        """
        error = f'❌ <Course [Estimated time field] Placeholder> of the Create course page - incorrect!'
        expect(self.course_form_estimated_time_field, error).to_have_attribute('placeholder', self.ESTIMATED_TIME_FIELD_PLACEHOLDER)

    def check_course_estimated_time_field_filled_correctly(self, estimated_time: str):
        """
        ✔ Check <Course [Estimated time field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param estimated_time: Estimated time
        """
        error = f'❌ <Course [Estimated time field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_estimated_time_field, error).to_have_value(estimated_time)


    # Course Form [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_course_description(self, description: str | None = None):
        """
        ✔ Check <Course [Description field]> of the Create course page

        If filled:
        ----------
        - ✔ Field - filled correctly

        If did not fill:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct

        :param description: Description (optional)
        """
        if description:   # If is passed
            self.check_course_description_field_filled_correctly(description)
        else:
            self.check_course_description_field_visible()
            self.check_course_description_field_name()
            self.check_course_description_field_placeholder()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_course_description_field_visible(self):
        """
        ✔ Check <Course [Description field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = f'❌ <Course [Description field]> of the Create course page - invisible!'
        expect(self.course_form_description_field, error).to_be_visible()

    def check_course_description_field_name(self):
        """
        ✔ Check <Course [Description field] name> of the Create course page - correct!

        - ✔ Field name - correct
        """
        error = f'❌ <Course [Description field] name> of the Create course page - incorrect!'
        expect(self.course_form_description_field, error).to_have_accessible_name(self.DESCRIPTION_FIELD_NAME)

    def check_course_description_field_placeholder(self):
        """
        ✔ Check <Course [Description field] Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct
        """
        error = f'❌ <Course [Description field] Placeholder> of the Create course page - incorrect!'
        expect(self.course_form_description_field, error).to_have_attribute('placeholder', self.DESCRIPTION_FIELD_PLACEHOLDER)

    def check_course_description_field_filled_correctly(self, description: str):
        """
        ✔ Check <Course [Description field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param description: Description
        """
        error = f'❌ <Course [Description field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_description_field, error).to_have_value(description)


    # Course Form [Max score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_course_max_score(self, max_score: str | None = None):
        """
        ✔ Check <Course [Max score field]> of the Create course page

        If filled:
        ----------
        - ✔ Field - filled correctly

        If did not fill:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field default value - correct

        :param max_score: Max score (optional)
        """
        if max_score:   # If is passed
            self.check_course_max_score_field_filled_correctly(max_score)
        else:
            self.check_course_max_score_field_visible()
            self.check_course_max_score_field_name()
            self.check_course_max_score_field_filled_correctly()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_course_max_score_field_visible(self):
        """
        ✔ Check <Course [Max score field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = f'❌ <Course [Max score field]> of the Create course page - invisible!'
        expect(self.course_form_max_score_field, error).to_be_visible()

    def check_course_max_score_field_name(self):
        """
        ✔ Check <Course [Max score field]> name of the Create course page - correct!

        - ✔ Field name - correct
        """
        error = f'❌ <Course [Max score field]> name of the Create course page - incorrect!'
        expect(self.course_form_max_score_field, error).to_have_accessible_name(self.MAX_SCORE_FIELD_NAME)

    def check_course_max_score_field_filled_correctly(self, max_score: str = '0'):
        """
        ✔ Check <Course [Max score field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param max_score: Max score
        """
        error = f'❌ <Course [Max score field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_max_score_field, error).to_have_value(max_score)


    # Course Form [Min score field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_course_min_score(self, min_score: str | None = None):
        """
        ✔ Check <Course [Min score field]> of the Create course page

        If filled:
        ----------
        - ✔ Field - filled correctly

        If did not fill:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field default value - correct

        :param min_score: Min score (optional)
        """
        if min_score:   # If is passed
            self.check_course_min_score_field_filled_correctly(min_score)
        else:
            self.check_course_min_score_field_visible()
            self.check_course_min_score_field_name()
            self.check_course_min_score_field_filled_correctly()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_course_min_score_field_visible(self):
        """
        ✔ Check <Course [Min score field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = f'❌ <Course§ [Min score field]> of the Create course page - invisible!'
        expect(self.course_form_min_score_field, error).to_be_visible()

    def check_course_min_score_field_name(self):
        """
        ✔ Check <Course [Min score field]> name of the Create course page - correct!

        - ✔ Field name - correct
        """
        error = f'❌ <Course [Min score field]> name of the Create course page - incorrect!'
        expect(self.course_form_min_score_field, error).to_have_accessible_name(self.MIN_SCORE_FIELD_NAME)

    def check_course_min_score_field_filled_correctly(self, min_score: str = '0'):
        """
        ✔ Check <Course [Min score field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param min_score: Min score
        """
        error = f'❌ <Course [Min score field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_min_score_field, error).to_have_value(min_score)

    # Exercises [Empty view] (component)
    # ──────────────────────────────────────────────────────╮
    def check_exercises_empty_view(self):
        """
        ✔ Check <Exercises [Empty view]>

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.exercises_empty_view.check_empty_view(
            title=self.EXERCISES_EMPTY_VIEW_TITLE,
            description=self.EXERCISES_EMPTY_VIEW_TITLE)
    # ──────────────────────────────────────────────────────╯
