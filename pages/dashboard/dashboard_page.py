"""
Dashboard page
"""

import allure
from config import Endpoint
from pages.base_page import BasePage
from playwright.sync_api import Page
from components.navigation.navbar.navbar_component import NavbarComponent
from components.navigation.sidebar.sidebar_component import SidebarComponent
from components.dashboard.toolbar_component import DashboardToolbarComponent
from components.dashboard.widget_component import DashboardWidgetComponent

#=======================================================================================================================
class DashboardPage(BasePage):
    """
    [Dashboard page]

    - Navbar (component)
    - Sidebar (component)
    - Toolbar (component)
    - Widgets (component)
    """
    URL = Endpoint.DASHBOARD

    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        # Bars
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = DashboardToolbarComponent(page)
        # Widgets
        self.student_widget = DashboardWidgetComponent(page=page, identifier='students', chart_type='bar')
        self.activities_widget = DashboardWidgetComponent(page=page, identifier='activities', chart_type='line')
        self.courses_widget = DashboardWidgetComponent(page=page, identifier='courses', chart_type='pie')
        self.scores_widget = DashboardWidgetComponent(page=page, identifier='scores', chart_type='scatter')


    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Page]
    # ──────────────────────────────────────┐
    @allure.step('✔ Check [Dashboard page]')
    def check(self, username: str):
        """
        ✔ Check [Dashboard page]

        - ✔ Navbar
        - ✔ Sidebar
        - ✔ Toolbar
        - ✔ Widgets
        """
        self.navbar.check(username)
        self.sidebar.check()
        self.toolbar.check()
        self.check_widgets()
    # ──────────────────────────────────────┘

    # [Widgets]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check all [Widgets]')
    def check_widgets(self):
        """
        ✔ Check all [Widgets]

        - ✔ Students - visible | - text | Chart - visible
        - ✔ Activities - visible | - text | Chart - visible
        - ✔ Courses - visible | - text | Chart - visible
        - ✔ Scores - visible | - text | Chart - visible
        """
        self.student_widget.check('Students')
        self.activities_widget.check('Activities')
        self.courses_widget.check('Courses')
        self.scores_widget.check('Scores')
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘


#=======================================================================================================================
