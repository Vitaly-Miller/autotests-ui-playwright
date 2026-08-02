"""
Dashboard page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class DashboardPage(BasePage):          # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('dashboard-toolbar-title-text')
        # ├ Navbar    <— ⚠️ ПЕРЕНЕСТИ в Components
        self.navbar_title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.navbar_welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')
        # ├ Widgets
        self.students_title = page.get_by_test_id('students-widget-title-text')
        self.students_chart = page.get_by_test_id('students-bar-chart')
        self.activities_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_chart = page.get_by_test_id('activities-bar-chart')
        self.courses_title = page.get_by_test_id('course-widget-title-text')
        self.courses_chart = page.get_by_test_id('courses-bar-chart')
        self.scores_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_chart = page.get_by_test_id('scores-bar-chart')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------



    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Navbar:
    def check_navbar_title(self, username: str):      # <— ⚠️ ПЕРЕНЕСТИ в Components
        """
        Check <Navbar> title

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ Welcome title - visible
        - ✔ Welcome title text - correct

        :param username: Username
        """
        error_navbar_title = '❌ Navbar title - invisible!'
        error_navbar_title_text = '❌ Navbar title text - incorrect!'
        error_welcome_title_visible = '❌ Navbar welcome title - invisible!'
        error_welcome_title_text = '❌ Navbar welcome title text - incorrect!'
        expect(self.navbar_title, error_navbar_title).to_be_visible()
        expect(self.navbar_title, error_navbar_title_text).to_have_text('UI Course')
        expect(self.navbar_welcome_title, error_welcome_title_visible).to_be_visible()
        expect(self.navbar_welcome_title, error_welcome_title_text).to_have_text(f'Welcome, {username}!')


    # Toolbar:
    def check_dashboard_toolbar_title(self):
        """
        Check <Toolbar> title of the Dashboard page

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        error_visible = '❌ <Toolbar> title of the Dashboard page - invisible!'
        error_text = '❌ <Toolbar> title text of the Dashboard page - incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text('Dashboard')


    # Widgets:
    def check_students_widget(self):
        """
        Check <Students widget> of the Dashboard page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ Chart - visible
        """
        error_title_visible = '❌ <Students widget> title text of the Dashboard page - invisible!'
        error_title_text = '❌ <Students widget> title text of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Students widget> chart of the Dashboard page - invisible!'
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
        error_title_visible = '❌ <Activities widget> title text of the Dashboard page - invisible!'
        error_title_text = '❌ <Activities widget> title text of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Activities widget> chart of the Dashboard page - invisible!'
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
        error_title_visible = '❌ <Courses widget> title text of the Dashboard page - invisible!'
        error_title_text = '❌ <Courses widget> title text of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Courses widget> chart of the Dashboard page - invisible!'
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
        error_title_visible = '❌ <Scores widget> title text of the Dashboard page - invisible!'
        error_title_text = '❌ <Scores widget> title text of the Dashboard page - incorrect!'
        error_chart_visible = '❌ <Scores widget> chart of the Dashboard page - invisible!'
        expect(self.scores_title, error_title_visible).to_be_visible()
        expect(self.scores_title, error_title_text).to_have_text('Scores')
        expect(self.scores_chart, error_chart_visible).to_be_visible()



#=======================================================================================================================
