"""
Create course page > [Toolbar] (component)
"""
import allure
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

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.toolbar_component = '❌ Create course page > Toolbar'
        self.title_element = f'{self.toolbar_component} > [Title]'
        self.create_course_btn_element = f'{self.toolbar_component} > [Create course button]'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('create-course-toolbar-create-course-button')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Create course button]
    @allure.step('▶ Click [Create course button]')
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
    # ─────────────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Toolbar]')
    def check(self, is_create_course_btn_enabled: bool = False):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Create course button - visible | - enabled / disabled
        """
        self.check_title()
        self.check_create_course_btn(enabled=is_create_course_btn_enabled)
    # ─────────────────────────────────────────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.check_title_visible()
        self.check_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Title]')
    def check_title_visible(self):
        """
        ✔ Check visible [Title]

        - ✔ Title - visible
        """
        error = f'{self.title_element} - invisible!'
        expect(self.title, error).to_be_visible()

    @allure.step('✔ Check text of [Title]')
    def check_title_text(self):
        """
        ✔ Check text of [Title]

        .
        """
        error = f'{self.title_element} - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # [Create course button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Create course button]')
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
    @allure.step('✔ Check visible [Create course button]')
    def check_create_course_btn_visible(self):
        """
        ✔ Check visible [Create course button]

        .
        """
        error = f'{self.create_course_btn_element} - invisible!'
        expect(self.create_course_btn, error).to_be_visible()

    @allure.step('✔ Check enabled [Create course button]')
    def check_create_course_btn_enabled(self):
        """
        ✔ Check enabled [Create course button]

        (If create course Form filled & Image uploaded)
        """
        error = f'{self.create_course_btn_element} - disabled!'
        expect(self.create_course_btn, error).to_be_enabled()

    @allure.step('✔ Check disabled [Create course button]')
    def check_create_course_btn_disabled(self):
        """
        ✔ Check disabled [Create course button]

        (If create course Form did NOT filled & Image did NOT upload)
        """
        error = f'{self.create_course_btn_element} - enabled!'
        expect(self.create_course_btn, error).to_be_disabled()


#=======================================================================================================================
