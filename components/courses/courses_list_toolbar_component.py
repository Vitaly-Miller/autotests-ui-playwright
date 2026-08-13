"""
Courses list [Toolbar] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


#=======================================================================================================================
"""
Elements:
- Title
- Create course button
"""
class CoursesListToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.TITLE_TEXT = 'Courses'
        self.CREATE_COURSE_PAGE_REDIRECT_URL = '/#/courses/create'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('courses-list-toolbar-create-course-button')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_create_course_btn(self):
        """
        ▶ Click [Create course button]

        - ✔ Button - visible
        - ▶ Button - click
        - ✔ Redirect new page URL - correct
        """
        self.check_create_course_btn_visible()
        self.create_course_btn.click()
        self.check_current_url(self.CREATE_COURSE_PAGE_REDIRECT_URL)


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ─────────────────────────────────┐
    def check_toolbar(self):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Create course button - visible
        """
        self.check_title()
        self.check_create_course_btn()
    # ─────────────────────────────────┘

    # Title
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Text - correct
        """
        self.check_title_visible()
        self.check_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self):
        """
        ✔ Check [Title]> visible

        - ✔ Title - visible
        """
        error = f'❌ <Toolbar [Title]> of the Courses list page - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'❌ Courses list page -> Toolbar -> [Title] - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)

    # Create course button
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_create_course_btn(self):
        """
         ✔ Check [Create course button]

        - ✔ Button - visible
        """
        self.check_create_course_btn_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_create_course_btn_visible(self):
        """
        ✔ Check [Create course button] visible

        .
        """
        error = f'❌ Courses list page -> Toolbar -> [Create course button] - invisible!'
        expect(self.create_course_btn, error).to_be_visible()


#=======================================================================================================================
