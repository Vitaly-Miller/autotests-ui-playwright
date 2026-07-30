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

        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        # ├ Buttons/Links
        self.create_course_btn = page.get_by_test_id('courses-list-toolbar-create-course-button')
        # ├ Items
        self.empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
        #
