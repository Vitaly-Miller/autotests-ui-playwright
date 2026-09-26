"""
Courses list page
"""

from config import Endpoint
from playwright.sync_api import Page
from components.courses.courses_list.course_card import CourseCardComponent
from pages.base_page import BasePage
from components.navigation.navbar.navbar import NavbarComponent
from components.navigation.sidebar.sidebar import SidebarComponent
from components.courses.courses_list.toolbar import CoursesListToolbarComponent
from components.views.empty_view import EmptyViewComponent

#=======================================================================================================================
class CoursesListPage(BasePage):
    """
    [Courses list page]

    - Navbar (component)
    - Sidebar (component)
    - Toolbar (component)
    - Empty view (component)
    - Course card (component)
    """
    URL = Endpoint.COURSES
    IDENTIFIER = 'courses-list'
    PATH = 'Courses list page'          # for logging

    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CoursesListToolbarComponent(page)
        self.empty_view = EmptyViewComponent(page=page, path=self.PATH, identifier=self.IDENTIFIER)
        self.course_card = CourseCardComponent(page)


    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # Courses list page [Empty view]:
    def check_empty_view(self):
        """
        ✔ Check  Courses list page [Empty view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.empty_view.check(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here')


#=======================================================================================================================
