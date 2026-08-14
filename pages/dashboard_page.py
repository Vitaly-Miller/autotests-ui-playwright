"""
Dashboard page
"""

from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.navigation.navbar.navbar_component import NavbarComponent
from components.navigation.sidebar.sidebar_component import SidebarComponent
from components.courses.dashboard.toolbar_component import DashboardToolbarComponent
from components.courses.dashboard.widget_component import DashboardWidgetComponent

#=======================================================================================================================
class DashboardPage(BasePage):          # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage
        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # # Students widgets
        # self.STUDENTS_WIDGET_IDENTIFIER = 'students'
        # self.STUDENTS_WIDGET_CHART_TYPE = 'bar'
        # self.STUDENTS_WIDGET_TITLE = 'Students'
        # # Activities widgets
        # self.ACTIVITIES_WIDGET_IDENTIFIER = 'activities'
        # self.ACTIVITIES_WIDGET_CHART_TYPE = 'line'
        # self.ACTIVITIES_WIDGET_TITLE = 'Activities'
        # # Courses widget
        # self.COURSES_WIDGET_IDENTIFIER = 'courses'
        # self.COURSES_WIDGET_CHART_TYPE = 'pie'
        # self.COURSES_WIDGET_TITLE = 'Courses'
        # # Scores widget
        # self.SCORES_WIDGET_IDENTIFIER = 'scores'
        # self.SCORES_WIDGET_CHART_TYPE = 'scatter'
        # self.SCORES_WIDGET_TITLE = 'Scores'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
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
    # [Widgets]
    # ───────────────────────────────────────────────────┐
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
    # ───────────────────────────────────────────────────┘



#=======================================================================================================================
