"""
Courses listpage
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class CoursesListPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ┌╴ 𝌆 DATA:
        # ├ Page
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
        # ├ Toolbar
        self.toolbar_title_text = 'Courses'
        # ├ Empty view
        self.empty_view_title_text = 'There is no results'
        self.empty_view_description_text = 'Results from the load test pipeline will be displayed here'


        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        # ├ Buttons/Links
        self.create_course_btn = page.get_by_test_id('courses-list-toolbar-create-course-button')
        # ├ Empty view
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_create_course_btn(self):
        """
        ▶ Actions:
        ----------
        - Click button

        ✔ Expectations:
        ---------------
        - Check button is visible
        """
        self.check_create_course_btn()
        self.create_course_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar
    def check_toolbar_title(self):
        """
        Check Toolbar title on the Courses List page

        - Title is visible
        - Title text is correct
        """
        error_visible = '❌ Toolbar title on the Courses List page is invisible!'
        error_text = '❌ Toolbar title text on the Courses List page is incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text(self.toolbar_title_text)

    def check_create_course_btn(self):
        """
        Check <Create course button>

        - Button is visible
        """
        error = '❌ Create course button on the Courses List page is invisible!'
        expect(self.create_course_btn, error).to_be_visible()


    # Empty view
    def check_empty_view(self):
        error_icon_visible = '❌ Empty view icon on the Courses List page is invisible!'
        error_title_visible = '❌ Empty view title on the Courses List page is invisible!'
        error_description_visible = '❌ Empty view description on the Courses List page is invisible!'
        error_title_text = '❌ Empty view title text on the Courses List page is incorrect!'
        error_description_text = '❌ Empty view description text on the Courses List page is incorrect!'
        expect(self.empty_view_icon, error_icon_visible).to_be_visible()
        expect(self.empty_view_title, error_title_visible).to_be_visible()
        expect(self.empty_view_description, error_description_visible).to_be_visible()
        expect(self.empty_view_title, error_title_text).to_have_text(self.empty_view_title_text)
        expect(self.empty_view_description, error_description_text).to_have_text(self.empty_view_description_text)
