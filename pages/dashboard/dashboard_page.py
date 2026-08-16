"""
Dashboard page
"""

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
        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # # [Students widget]
        # self.STUDENTS_WIDGET_IDENTIFIER = 'students'
        # self.STUDENTS_WIDGET_CHART_TYPE = 'bar'
        # self.STUDENTS_WIDGET_TITLE = 'Students'
        # # [Activities widget]
        # self.ACTIVITIES_WIDGET_IDENTIFIER = 'activities'
        # self.ACTIVITIES_WIDGET_CHART_TYPE = 'line'
        # self.ACTIVITIES_WIDGET_TITLE = 'Activities'
        # # [Courses widget]
        # self.COURSES_WIDGET_IDENTIFIER = 'courses'
        # self.COURSES_WIDGET_CHART_TYPE = 'pie'
        # self.COURSES_WIDGET_TITLE = 'Courses'
        # # [Scores widget]
        # self.SCORES_WIDGET_IDENTIFIER = 'scores'
        # self.SCORES_WIDGET_CHART_TYPE = 'scatter'
        # self.SCORES_WIDGET_TITLE = 'Scores'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        # <Bars>
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = DashboardToolbarComponent(page)
        # <Widgets>
        self.student_widget = DashboardWidgetComponent(page=page, identifier='students', chart_type='bar')
        self.activities_widget = DashboardWidgetComponent(page=page, identifier='activities', chart_type='line')
        self.courses_widget = DashboardWidgetComponent(page=page, identifier='courses', chart_type='pie')
        self.scores_widget = DashboardWidgetComponent(page=page, identifier='scores', chart_type='scatter')

        # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Page]
    # ─────────────────────────────────────┐
    def check_page(self, username: str):
        """
        ✔ Check [Dashboard page] elements

        - ✔ Navbar
        - ✔ Sidebar
        - ✔ Toolbar
        - ✔ Widgets
        """
        self.navbar.check_navbar(username)
        self.sidebar.check_sidebar()
        self.toolbar.check_toolbar()
        self.check_widgets()
    # ─────────────────────────────────────┘

    # [Widgets]
    # # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_widgets(self):
        """
        ✔ Check all Widgets

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
