"""
Courses list page
"""
from components.courses.coureses_list.course_view_component import CoursesListCourseViewComponent
from pages.base_page import BasePage
from components.navigation.navbar.navbar_component import NavbarComponent
from components.navigation.sidebar.sidebar_component import SidebarComponent
from components.courses.coureses_list.toolbar_component import CoursesListToolbarComponent
from components.views.emty_view_component import EmptyViewComponent

from playwright.sync_api import Page

#=======================================================================================================================
class CoursesListPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.IDENTIFIER = 'courses-list'
        self.EMPTY_VIEW_TITLE = 'There is no results'
        self.EMPTY_VIEW_DESCRIPTION = 'Results from the load test pipeline will be displayed here'

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CoursesListToolbarComponent(page)
        self.empty_view = EmptyViewComponent(page=page, identifier=self.IDENTIFIER)
        self.course_view = CoursesListCourseViewComponent(page)


    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # Empty view (component):
    def check_empty_view(self):
        """
        ✔ Check <Empty view> component of the Courses list page

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.empty_view.check_empty_view(
            title=self.EMPTY_VIEW_TITLE,
            description=self.EMPTY_VIEW_DESCRIPTION)


#=======================================================================================================================
