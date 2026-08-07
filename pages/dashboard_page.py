"""
Dashboard page
"""

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
class DashboardPage(BasePage):          # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ----------------------------------------------- ⿷ COMPONENTS ------------------------------------------------
        self.navbar = NavbarComponent(page)   # Component - Navbar

        # -------------------------------------------- ㉧ LOCATORS (static) ---------------------------------------------
        # Toolbar
        self.toolbar_title = page.get_by_test_id('dashboard-toolbar-title-text')
        # Widgets
        self.students_title = page.get_by_test_id('students-widget-title-text')
        self.students_chart = page.get_by_test_id('students-bar-chart')
        self.activities_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_chart = page.get_by_test_id('activities-line-chart')
        self.courses_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_chart = page.get_by_test_id('courses-pie-chart')
        self.scores_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_chart = page.get_by_test_id('scores-scatter-chart')


    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------



    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # <Navbar> + <Toolbar>
    # ────────────────────────────────────────────────┐
    def check_navbar_and_toolbar(self, username: str):
        """
        Check <Navbar> + <Toolbar> of the Dashboard page

        - ✔ Navbar - visible | Text - correct
        - ✔ Toolbar - visible | Text - correct
        """
        self.navbar.check_navbar(username)
        self.check_toolbar()
    # ────────────────────────────────────────────────┘

    # Toolbar:
    # ──────────────────────────────────────┐
    def check_toolbar(self):
        """
        Check <Toolbar> of the Dashboard page

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        self.check_toolbar_title_visible()
        self.check_toolbar_title_text()
    # ──────────────────────────────────────┘
    def check_toolbar_title_visible(self):
        """
        Check <Toolbar [Title]> of the Dashboard page

        - ✔ Title - visible

        """
        error = '❌ <Toolbar [Title]> of the Dashboard page - invisible!'
        expect(self.toolbar_title, error).to_be_visible()

    def check_toolbar_title_text(self):
        """
        Check <Toolbar [Title] text> of the Dashboard page

        - ✔ Text - correct
        """
        error = '❌ <Toolbar [Title] text> of the Dashboard page - incorrect!'
        expect(self.toolbar_title, error).to_have_text('Dashboard')


    # Widgets:
    # ─────────────────────────────────┐
    def check_all_widgets(self):
        """
        Check all Widgets of the Dashboard page

        - ✔ Students - visible | Text - correct | Chart - visible
        - ✔ Activities - visible | Text - correct | Chart - visible
        - ✔ Courses - visible | Text - correct | Chart - visible
        - ✔ Scores - visible | Text - correct | Chart - visible
        """
        self.check_students_widget()
        self.check_activities_widget()
        self.check_courses_widget()
        self.check_scores_widget()
    # ─────────────────────────────────┘

    def check_students_widget(self):
        """
        Check <Students widget> of the Dashboard page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ Chart - visible
        """
        error_title_visible = '❌ <Students widget [Title]> of the Dashboard page - invisible!'
        error_title_text = '❌ <Students widget [Title] text> of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Students widget [Chart]> of the Dashboard page - invisible!'
        expect(self.students_title, error_title_visible).to_be_visible()
        expect(self.students_title, error_title_text).to_have_text('Students')
        expect(self.students_chart, error_chart_visible).to_be_visible()

    def check_activities_widget(self):
        """
        Check <Activities widget> of the Dashboard page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ Chart - visible
        """
        error_title_visible = '❌ <Activities widget [Title]> of the Dashboard page - invisible!'
        error_title_text = '❌ <Activities widget [Title] text>  of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Activities widget [Chart]> of the Dashboard page - invisible!'
        expect(self.activities_title, error_title_visible).to_be_visible()
        expect(self.activities_title, error_title_text).to_have_text('Activities')
        expect(self.activities_chart, error_chart_visible).to_be_visible()

    def check_courses_widget(self):
        """
        Check <Courses widget> of the Dashboard page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ Chart - visible
        """
        error_title_visible = '❌ <Courses widget [Title]> of the Dashboard page - invisible!'
        error_title_text = '❌ <Courses widget [Title] text> of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Courses widget [Chart]> of the Dashboard page - invisible!'
        expect(self.courses_title, error_title_visible).to_be_visible()
        expect(self.courses_title, error_title_text).to_have_text('Courses')
        expect(self.courses_chart, error_chart_visible).to_be_visible()

    def check_scores_widget(self):
        """
        Check <Scores widget> of the Dashboard page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ Chart - visible
        """
        error_title_visible = '❌ <Scores widget [Title]> of the Dashboard page - invisible!'
        error_title_text = '❌ <Scores widget [Title] text> of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Scores widget [Chart]> of the Dashboard page - invisible!'
        expect(self.scores_title, error_title_visible).to_be_visible()
        expect(self.scores_title, error_title_text).to_have_text('Scores')
        expect(self.scores_chart, error_chart_visible).to_be_visible()



#=======================================================================================================================
