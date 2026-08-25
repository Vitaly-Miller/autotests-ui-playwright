"""
Create Course page
"""
import allure

from pages.base_page import BasePage
from playwright.sync_api import Page
from components.navigation.navbar.navbar_component import NavbarComponent
from components.navigation.sidebar.sidebar_component import SidebarComponent
from components.courses.create_course.toolbar_component import CreateCourseToolbarComponent
from components.views.emty_view_component import EmptyViewComponent
from components.courses.create_course.image_upload_widget_component import CreateCourseImageUploadWidgetComponent
from components.courses.create_course.form_component import CreateCourseFormComponent
from components.courses.create_course.exercises_toolbar_component import CreateCourseExercisesToolbarComponent
from components.courses.create_course.exercise_component import CreateCourseExerciseComponent

#=======================================================================================================================
"""
[Create Course page]
- Empty view (component)
- Image upload widget (component)
- Form (component)
- Exercises toolbar (component)
- Exercise (component)
"""
class CreateCoursePage(BasePage):        # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'

    def __init__(self, page: Page):      # Конструктор класса, принимающий Page
        super().__init__(page)           # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.COMPONENT = 'Create Course page'
        self.EXERCISES_IDENTIFIER = 'create-course-exercises'
        self.EXERCISES_EMPTY_VIEW_TITLE = 'There is no exercises'
        self.EXERCISES_EMPTY_VIEW_DESCRIPTION = 'Click on "Create exercise" button to create new exercise'

        # ----------------------------------------------- ⿳ COMPONENTS ------------------------------------------------
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CreateCourseToolbarComponent(page)
        self.image_upload_widget = CreateCourseImageUploadWidgetComponent(page)
        self.form = CreateCourseFormComponent(page)
        self.exercises_toolbar = CreateCourseExercisesToolbarComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page=page, identifier=self.EXERCISES_IDENTIFIER, component=self.COMPONENT)
        self.exercise = CreateCourseExerciseComponent(page)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Exercises [Empty view]
    # ───────────────────────────────────────────────────┐
    @allure.step('✔ Check Exercises [Empty view]')
    def check_exercises_empty_view(self):
        """
        ✔ Check Exercises [Empty view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.exercises_empty_view.check(
            title=self.EXERCISES_EMPTY_VIEW_TITLE,
            description=self.EXERCISES_EMPTY_VIEW_TITLE)
    # ───────────────────────────────────────────────────┘
