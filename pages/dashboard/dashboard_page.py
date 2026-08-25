"""
Dashboard page
"""
import allure

from pages.base_page import BasePage
from playwright.sync_api import Page
from components.navigation.navbar.navbar_component import NavbarComponent
from components.navigation.sidebar.sidebar_component import SidebarComponent
from components.dashboard.toolbar_component import DashboardToolbarComponent
from components.dashboard.widget_component import DashboardWidgetComponent

#=======================================================================================================================
class DashboardPage(BasePage):          # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ----------------------------------------------- ⿳ COMPONENTS ------------------------------------------------
        # Bars
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = DashboardToolbarComponent(page)
        # Widgets
        self.student_widget = DashboardWidgetComponent(page=page, identifier='students', chart_type='bar')
        self.activities_widget = DashboardWidgetComponent(page=page, identifier='activities', chart_type='line')
        self.courses_widget = DashboardWidgetComponent(page=page, identifier='courses', chart_type='pie')
        self.scores_widget = DashboardWidgetComponent(page=page, identifier='scores', chart_type='scatter')

        # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Page]
    # ─────────────────────────────┐
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
    # ─────────────────────────────┘

    # [Widgets]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check all [Widgets]')
    def check_widgets(self):
        """
        ✔ Check all [Widgets]

        - ✔ Students - visible | - text | Chart - visible
        - ✔ Activities - visible | - text | Chart - visible
        - ✔ Courses - visible | - text | Chart - visible
        - ✔ Scores - visible | - text | Chart - visible
        """
        self.student_widget.check_widget('Students')
        self.activities_widget.check_widget('Activities')
        self.courses_widget.check_widget('Courses')
        self.scores_widget.check_widget('Scores')
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘



#=======================================================================================================================
