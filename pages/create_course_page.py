"""
Create Course page
"""

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.emty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from playwright.sync_api import Locator, Page, expect

#=======================================================================================================================
class CreateCoursePage(BasePage):        # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'

    def __init__(self, page: Page):      # Конструктор класса, принимающий Page
        super().__init__(page)           # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        # Toolbar
        self.TOOLBAR_TITLE = 'Create course'


        # Course [Form]
        self.TITLE_FIELD_NAME = 'Title'
        self.TITLE_FIELD_PLACEHOLDER = 'New course'
        self.ESTIMATED_TIME_FIELD_NAME = 'Estimated time'
        self.ESTIMATED_TIME_FIELD_PLACEHOLDER = '1h 20m'
        self.DESCRIPTION_FIELD_NAME = 'Description'
        self.DESCRIPTION_FIELD_PLACEHOLDER = 'Add description for course'
        self.MAX_SCORE_FIELD_NAME = 'Max score'
        self.MIN_SCORE_FIELD_NAME = 'Min score'

        # Exercises [Toolbar]
        self.EXERCISES_TOOLBAR_TITLE = 'Exercises'
        self.EXERCISE_TOOLBAR_TITLE_PART_TEXT = 'Exercise'   # Part of text (Ex: "#1 Exercise")

        # Exercises [Empty view]
        self.EXERCISES_EMPTY_VIEW_IDENTIFIER = 'create-course-exercises'
        self.EXERCISES_EMPTY_VIEW_TITLE = 'There is no exercises'
        self.EXERCISES_EMPTY_VIEW_DESCRIPTION = 'Click on "Create exercise" button to create new exercise'

        # Exercises [Exercise]
        self.EXERCISE_TITLE_FIELD_NAME = 'Title'
        self.EXERCISE_DESCRIPTION_FIELD_NAME = 'Description'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page=page, identifier=self.EXERCISES_EMPTY_VIEW_IDENTIFIER)

        # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------
        # Toolbar
        self.toolbar_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('create-course-toolbar-create-course-button')



        # Course Form
        self.course_form_title_field = page.get_by_role(role='textbox', name='Title')
        self.course_form_estimated_time_field = page.get_by_role(role='textbox', name='Estimated time')
        self.course_form_description_field = page.get_by_role(role='textbox', name='Description')
        self.course_form_max_score_field = page.get_by_role(role='spinbutton', name='Max score')
        self.course_form_min_score_field = page.get_by_role(role='spinbutton', name='Min score')

        # EXERCISES:
        # Exercises [Toolbar]
        self.exercise_toolbar_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercise_toolbar_create_exercise_btn = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        # Exercises [Empty view]
        # See —> /components/views/empty_view_component.py

        # Exercises [Exercise]
        # ┄┄┄┄┄┄┄┄ (lambda - index) - ⚠️ NOT USING! - FOR EXAMPLE ONLY ┄┄┄┄┄┄┄┄╮
        self._exercise_subtitle = lambda index=0: page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        self._delete_exercise_btn = lambda index=0: page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        self._exercise_title_field = lambda index=0: page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        self._exercise_description_field = lambda index=0: page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')
        # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ⬇︎ use dynamic def-locators ⬇︎ ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╯


    # ---------------------------------------------- ㉤ LOCATORS {dynamic} ----------------------------------------------
    # EXERCISES: —> index: Element index
    # - Exercise
    def exercise_subtitle(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')

    def delete_exercise_btn(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')

    # - Exercise Form
    def exercise_form_title_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

    def exercise_form_description_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------

    def click_create_course_btn(self):
        """
        Click <Create course Button> of the Create course page

        - ✔ Button - visible
        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_toolbar_create_course_btn_visible()
        self.check_toolbar_create_course_btn_enabled()
        self.create_course_btn.click()


    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str):
        """
        Fill Create course form of the Create course page

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

    # EXERCISES:
    def click_create_exercise_btn(self):
        """
        Click <Create exercise Button> of the Create course page

        - ✔ Button - visible
        - ▶ Button - click
        """
        self.check_exercises_toolbar_create_exercise_btn_visible()
        self.exercise_toolbar_create_exercise_btn.click()

    def click_delete_exercise_btn(self, index: int):
        """
        Click <Delete exercise Button> of the Create course page

        - ✔ Button - visible
        - ▶ Button - click

        :param index: Exercise index
        """
        self.check_delete_exercise_btn_visible(index)
        self.delete_exercise_btn(index).click()


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

    # Toolbar [Create Course Button]
    def check_toolbar_create_course_btn_visible(self):
        """
        ✔ Check <Toolbar [Create Course Button]> of the Create course page - visible

        - ✔ Button - visible
        """
        error = f'❌ <Toolbar [Create Course Button]> of the Create course page - invisible!'
        expect(self.create_course_btn, error).to_be_visible()

    def check_toolbar_create_course_btn_enabled(self):
        """
        ✔ Check <Toolbar [Create Course Button]> of the Create course page - enabled

        - ✔ Button - enabled
        """
        error = f'❌ <Toolbar [Create Course Button]> of the Create course page - disabled!'
        expect(self.create_course_btn, error).to_be_enabled()

    def check_toolbar_create_course_btn_disabled(self):
        """
        ✔ Check <Toolbar [Create Course Button]> of the Create course page - disabled

        - ✔ Button - disabled
        """
        error = f'❌ <Toolbar [Create Course Button]> of the Create course page - enabled!'
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



    # EXERCISES:
    # Exercises [Toolbar]
    # ──────────────────────────────────────────────────────────────┐
    def check_exercises_toolbar(self):
        """
        ✔ Check <Exercises [Toolbar]> of the Create course page

        - ✔ Title - visible
        - ✔ Text - correct
        - ✔ Create exercise Button - correct

        """
        self.check_exercises_toolbar_title_visible()
        self.check_exercises_toolbar_title_text()
        self.check_exercises_toolbar_create_exercise_btn_visible()
    # ──────────────────────────────────────────────────────────────┘
    # Exercises Toolbar [Title]
    def check_exercises_toolbar_title_visible(self):
        """
        ✔ Check <Exercises Toolbar [Title]> of the Create course page - visible

        - ✔ Title - visible
        """
        error = f'❌ <Exercises Toolbar [Title]> of the Create course page - invisible!'
        expect(self.exercise_toolbar_title, error).to_be_visible()

    def check_exercises_toolbar_title_text(self):
        """
        ✔ Check <Exercises Toolbar [Title] text> of the Create course page - correct

        - ✔ Text - correct
        """
        error = f'❌ <Exercises Toolbar [Title] text> of the Create course page - incorrect!'
        expect(self.exercise_toolbar_title, error).to_have_text(self.EXERCISES_TOOLBAR_TITLE)

    # Exercises Toolbar [Create exercise button]
    def check_exercises_toolbar_create_exercise_btn_visible(self):
        """
        ✔ Check <Exercises Toolbar [Create exercise Button]> of the Create course page - visible

        - ✔ Button - visible
        """
        error = f'❌ <Exercises Toolbar [Create exercise Button]> of the Create course page - invisible!'
        expect(self.exercise_toolbar_create_exercise_btn, error).to_be_visible()


    # Exercises [Empty view] (component)
    # ──────────────────────────────────────────────────────╮
    def check_exercises_empty_view(self):
        """
        ✔ Check ALL elements of the <Exercise [Empty view]> component of the  Create course page

        - ✔ Icon - visible
        - ✔ Title - visible | Text - correct
        - ✔ Description - visible | Text - correct
        """
        self.preview_empty_view.check_component(
            title=self.PREVIEW_EMPTY_VIEW_TITLE,
            description=self.PREVIEW_EMPTY_VIEW_DESCRIPTION)
    # ──────────────────────────────────────────────────────╯


    # Exercise [Toolbar]
    # ───────────────────────────────────────────────┐
    def check_exercise_toolbar(self, index: int = 0):
        """
        ✔ Check <Exercises Toolbar> of the Create course page

        - ✔ Title - visible
        - ✔ Text - correct
        - ✔ Delete exercise Button - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.check_exercise_toolbar_title_visible(index)
        self.check_exercise_toolbar_title_text(index)
        self.check_delete_exercise_btn_visible(index)
    # ───────────────────────────────────────────────┘
    # Exercise Toolbar [Title]
    def check_exercise_toolbar_title_visible(self, index: int = 0):
        """
        ✔ Check <Exercise Toolbar [Title]> of the Create course page - visible

        - ✔ Title - visible

        :param index: Locator Index (ex: ...-exercise-{index}-box-toolbar-...)
        """
        error = f'❌ <Exercise Toolbar [Title]> of the Create course page - invisible!'
        expect(self.exercise_subtitle(index), error).to_be_visible()

    def check_exercise_toolbar_title_text(self, index: int = 0):
        """
        ✔ Check <Exercise Toolbar [Title] text> of the Create course page - correct

        - ✔ Text - correct (Ex: "#1 Exercise", "#2 Exercise", ...)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ <Exercise Toolbar [Title] text> of the Create course page - incorrect!'
        expect(self.exercise_subtitle(index), error).to_have_text(f'#{index + 1} {self.EXERCISE_TOOLBAR_TITLE_PART_TEXT}')

    # - Exercise [Delete exercise Button]
    def check_delete_exercise_btn_visible(self, index: int = 0):
        """
        ✔ Check <Exercise Toolbar [Delete exercise Button]> of the Create course page - visible

        - ✔ Button - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ <Exercise Toolbar [Delete exercise Button]> of the Create course page - invisible!'
        expect(self.delete_exercise_btn(index), error).to_be_visible()



    # Exercise [Form]
    # ──────────────────────────────────────────────────────────────────────────────────┐
    def check_exercise_form(self, index: int = 0, title: str | None = None, description: str | None = None):
        """
        ✔ Check <Exercise Form> of the Create course page

        - ✔ Fields - visible
        - ✔ Field names - correct
        - ✔ Fields - filled correctly (If filled)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        :param description: Exercise description
        """
        self.check_exercise_title_field(index=index, title=title)
        self.check_exercise_description_field(index=index, description=description)
    # ──────────────────────────────────────────────────────────────────────────────────┘

    # Exercise [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_exercise_title_field(self, index: int = 0, title: str | None = None):
        """
        ✔ Check <Exercise Form [Title field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - default value - correctly
        - ✔ Field - filled correctly (If is passed)
        - ✔ Field - default value correct (If is NOT passed)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        """
        self.check_exercise_title_field_visible(index)
        self.check_exercise_title_field_name(index)
        if title:   # If is passed
            self.check_exercise_title_field_filled_correctly(index=index, title=title)
        else:       # If is NOT passed (will check default value)
            self.check_exercise_title_field_filled_correctly(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_exercise_title_field_visible(self, index: int = 0):
        """
        ✔ Check <Exercise [Title field]> of the Create course page - visible

        - ✔ Field - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ <Exercise [Title field]> of the Create course page - invisible!'
        expect(self.exercise_form_title_field(index), error).to_be_visible()

    def check_exercise_title_field_name(self, index: int = 0):
        """
        ✔ Check <Exercise [Title field] name> of the Create course page - correct

        - ✔ Field - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ <Exercise [Title field] name> of the Create course page - incorrect!'
        expect(self.exercise_form_title_field(index), error).to_have_accessible_name(self.EXERCISE_TITLE_FIELD_NAME)

    def check_exercise_title_field_filled_correctly(self, index: int = 0, title: str = 'Exercise title'):
        """
        ✔ Check <Exercise [Title field]> of the Create course page - filled correctly

        If is passed:
        ------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - value correct (by default)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title

        """
        error = f'❌ <Exercise [Title field]> of the Create course page - filled incorrectly!'
        expect(self.exercise_form_title_field(index), error).to_have_value(title)


    # Exercise [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_exercise_description_field(self, index: int = 0, description: str | None = None):
        """
        ✔ Check <Exercise Form [Description field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - default value - correctly
        - ✔ Field - filled correctly (If is passed)
        - ✔ Field - default value correct (If is NOT passed)


        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description
        """
        self.check_exercise_description_field_visible(index)
        self.check_exercise_description_field_name(index)
        if description:  # If is passed
            self.check_exercise_description_field_filled_correctly(index=index, description=description)
        else:            # If is NOT passed (will check default value)
            self.check_exercise_description_field_filled_correctly(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_exercise_description_field_visible(self, index: int = 0):
        """
        ✔ Check <Exercise [Description field]> of the Create course page - visible

        - ✔ Field - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ <Exercise [Description field]> of the Create course page - invisible!'
        expect(self.exercise_form_description_field(index), error).to_be_visible()

    def check_exercise_description_field_name(self, index: int = 0):
        """
        ✔ Check <Exercise [Description field] name> of the Create course page - correct

        - ✔ Field name - correct

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ <Exercise [Description field] name> of the Create course page - incorrect!'
        expect(self.exercise_form_description_field(index), error).to_have_accessible_name(self.EXERCISE_DESCRIPTION_FIELD_NAME)

    def check_exercise_description_field_filled_correctly(self, index: int = 0, description: str = 'Exercise description'):
        """
        ✔ Check <Exercise [Description field]> of the Create course page - filled correctly

        If is passed:
        ------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - value correct (by default)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description
        """
        error = f'❌ <Exercise [Description field]> of the Create course page - filled incorrectly!'
        expect(self.exercise_form_description_field(index), error).to_have_value(description)
