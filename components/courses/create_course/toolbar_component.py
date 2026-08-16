"""
Create course page > [Toolbar] (component)
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


#=======================================================================================================================
"""
[Toolbar]:
- Title
- Create course button
"""
class CreateCourseToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.TITLE_TEXT = 'Create course'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('create-course-toolbar-create-course-button')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Create course button]
    def click_create_course_btn(self):
        """
        ▶ Click [Create course button]

        - ✔ Button - visible | - enabled
        - ▶ Button - click
        """
        self.check_create_course_btn(enabled=True)
        self.create_course_btn.click()



    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Toolbar]
    # ─────────────────────────────────┐
    def check_toolbar(self, is_create_course_btn_enabled: bool = False):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Create course button - visible | - enabled / disabled
        """
        self.check_title()
        self.check_create_course_btn(enabled=is_create_course_btn_enabled)
    # ─────────────────────────────────┘

    # [Title]
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
        error = f'❌ Create course page > Toolbar > [Title]> - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'❌ Create course page > Toolbar > [Title] - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # [Create course button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_create_course_btn(self, enabled: bool = False):
        """
         ✔ Check [Create course button]

        - ✔ Button - visible
        - ✔ Button - enabled / disabled
        """
        self.check_create_course_btn_visible()
        if enabled:
            self.check_create_course_btn_enabled()
        else:
            self.check_create_course_btn_disabled()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_create_course_btn_visible(self):
        """
        ✔ Check [Create course button] visible

        .
        """
        error = f'❌ Create course page > Toolbar > [Create course button] - invisible!'
        expect(self.create_course_btn, error).to_be_visible()

    def check_create_course_btn_enabled(self):
        """
        ✔ Check [Create course button] enabled

        (If create course Form filled & Image uploaded)
        """
        error = f'❌ Create course page > Toolbar > [Create course button] - disabled!'
        expect(self.create_course_btn, error).to_be_enabled()

    def check_create_course_btn_disabled(self):
        """
        ✔ Check [Create course button] disabled

        (If create course Form did NOT filled & Image did NOT upload)
        """
        error = f'❌ Create course page > Toolbar > [Create course button] - enabled!'
        expect(self.create_course_btn, error).to_be_disabled()


#=======================================================================================================================
