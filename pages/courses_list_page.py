"""
Courses List page
"""

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.courses_list_toolbar_component import CoursesListToolbarComponent
from components.views.emty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from playwright.sync_api import Page

#=======================================================================================================================
class CoursesListPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # 𝌆 DATA:
        self.IDENTIFIER = 'courses-list'
        self.EMPTY_VIEW_TITLE = 'There is no results'
        self.EMPTY_VIEW_DESCRIPTION = 'Results from the load test pipeline will be displayed here'

        # ⿴ COMPONENTS:
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CoursesListToolbarComponent(page)
        self.empty_view = EmptyViewComponent(page=page, identifier=self.IDENTIFIER)
        self.course_view = CourseViewComponent(page)


    # ✔️EXPECTATIONS:

    # Empty view (component):
    def check_empty_view(self):
        """
        ✔ Check <Empty view> component of the Courses List page

        - ✔ Icon - visible
        - ✔ Title - visible | Text - correct
        - ✔ Description - visible | Text - correct
        """
        self.empty_view.check_component(
            title=self.EMPTY_VIEW_TITLE,
            description=self.EMPTY_VIEW_DESCRIPTION)


#=======================================================================================================================
