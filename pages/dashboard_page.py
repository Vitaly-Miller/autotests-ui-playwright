"""
Dashboard page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, Locator, expect

#=======================================================================================================================
class DashboardPage(BasePage):          # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ┌╴ 𝌆 DATA:
        # ├ Page
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        # ├ Toolbar
        self.toolbar_title_text = 'Dashboard'
        # ├ Navbar <— ⚠️ ПЕРЕНЕСТИ в Components
        self.navbar_title_text = 'UI Course'
        self.navbar_welcome_title_text = 'Welcome, '   # <— static part of the dynamic text
        # ├ Widgets
        self.students_title_text = 'Students'
        self.activities_title_text = 'Activities'
        self.courses_title_text = 'Courses'
        self.scores_title_text = 'Scores'


        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('dashboard-toolbar-title-text')
        # ├ Navbar <— ⚠️ ПЕРЕНЕСТИ в Components
        self.navbar_title = page.get_by_test_id('navigation-navbar-app-title-text')
        # ├ Widgets
        self.students_title = page.get_by_test_id('students-widget-title-text')
        self.students_chart = page.get_by_test_id('students-bar-chart')
        self.activities_title = page.get_by_test_id('activities-widget-title-text')
        self.activities_chart = page.get_by_test_id('activities-bar-chart')
        self.courses_title = page.get_by_test_id('course-widget-title-text')
        self.courses_chart = page.get_by_test_id('courses-bar-chart')
        self.scores_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_chart = page.get_by_test_id('scores-bar-chart')

    # ┌╴ ㉧ LOCATORS {dynamic}:
    # ├ Navbar
    def navbar_welcome_title(self, username: str) -> Locator:
        return self.page.get_by_text(text=f'Welcome, {username}!')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------



    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Navbar:
    def check_navbar_title(self, username: str):  # <— ⚠️ ПЕРЕНЕСТИ в Components
        """
        Check Navbar title

        :param username: Username

        - Title is visible
        - Title text is correct
        - Welcome title is visible
        - Welcome title text is correct (ex: Welcome, John!)
        """
        error_navbar_title = '❌ Navbar title is invisible!'
        error_navbar_title_text = '❌ Navbar title text is incorrect!'
        error_welcome_title_visible = '❌ Navbar welcome title is invisible!'
        error_welcome_title_text = '❌ Navbar welcome title text is incorrect!'
        expect(self.navbar_title, error_navbar_title).to_be_visible()
        expect(self.navbar_title, error_navbar_title_text).to_have_text(self.navbar_title_text)
        expect(self.navbar_welcome_title(username), error_welcome_title_visible).to_be_visible()
        expect(self.navbar_welcome_title(username), error_welcome_title_text).to_have_text(f'{self.navbar_welcome_title_text}{username}!')


    # Toolbar:
    def check_toolbar_title(self):
        """
        Check Toolbar title text on the Dashboard page

        - Title is visible
        - Title text is correct
        """
        error_visible = '❌ Toolbar title is invisible on the Dashboard page!'
        error_text = '❌ Toolbar title text on the Dashboard page is incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text(self.toolbar_title_text)


    # Widgets:
    def check_students_widget(self):
        """
        Check Students widget on the Dashboard page

        - Title is visible
        - Title text is correct
        - Chart is visible
        """
        error_title_visible = '❌ Students widget title text is invisible on the Dashboard page!'
        error_title_text = '❌ Students widget title text on the Dashboard page is incorrect!'
        error_chart_visible = '❌ Students widget chart is not visible on the Dashboard page!'
        expect(self.students_title, error_title_visible).to_be_visible()
        expect(self.students_title, error_title_text).to_have_text(self.students_title_text)
        expect(self.students_chart, error_chart_visible).to_be_visible()


    def check_activities_widget(self):
        """
        Check Activities widget on the Dashboard page

        - Title is visible
        - Title text is correct
        - Chart is visible
        """
        error_title_visible = '❌ Activities widget title text is invisible on the Dashboard page!'
        error_title_text = '❌ Activities widget title text on the Dashboard page is incorrect!'
        error_chart_visible = '❌ Activities widget chart is not visible on the Dashboard page!'
        expect(self.activities_title, error_title_visible).to_be_visible()
        expect(self.activities_title, error_title_text).to_have_text(self.activities_title_text)
        expect(self.activities_chart, error_chart_visible).to_be_visible()


    def check_courses_widget(self):
        """
        Check Courses widget on the Dashboard page

        - Title is visible
        - Title text is correct
        - Chart is visible
        """
        error_title_visible = '❌ Courses widget title text is invisible on the Dashboard page!'
        error_title_text = '❌ Courses widget title text on the Dashboard page is incorrect!'
        error_chart_visible = '❌ Courses widget chart is not visible on the Dashboard page!'
        expect(self.courses_title, error_title_visible).to_be_visible()
        expect(self.courses_title, error_title_text).to_have_text(self.courses_title_text)
        expect(self.courses_chart, error_chart_visible).to_be_visible()


    def check_scores_widget(self):
        """
        Check Scores widget on the Dashboard page

        - Title is visible
        - Title text is correct
        - Chart is visible
        """
        error_title_visible = '❌ Scores widget title text is invisible on the Dashboard page!'
        error_title_text = '❌ Scores widget title text on the Dashboard page is incorrect!'
        error_chart_visible = '❌ Scores widget chart is not visible on the Dashboard page!'
        expect(self.scores_title, error_title_visible).to_be_visible()
        expect(self.scores_title, error_title_text).to_have_text(self.scores_title_text)
        expect(self.scores_chart, error_chart_visible).to_be_visible()



#=======================================================================================================================
