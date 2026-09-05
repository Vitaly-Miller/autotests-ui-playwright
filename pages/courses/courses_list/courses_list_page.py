"""
Courses list page
"""

from config import Endpoint
from playwright.sync_api import Page
from components.courses.courses_list.course_card_component import CourseCardComponent
from pages.base_page import BasePage
from components.navigation.navbar.navbar_component import NavbarComponent
from components.navigation.sidebar.sidebar_component import SidebarComponent
from components.courses.courses_list.toolbar_component import CoursesListToolbarComponent
from components.views.empty_view_component import EmptyViewComponent

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
