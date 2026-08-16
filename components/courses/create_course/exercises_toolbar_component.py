"""
Create course page > Exercises > [Toolbar] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
[Toolbar]:
- Title
- Create exercise button
"""
class CreateCourseExercisesToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.TITLE_TEXT = 'Exercises'

        # ---------------------------------------------- ㉤ LOCATORS ----------------------------------------------------
        self.title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_btn = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Create exercise button]
    def click_create_exercise_btn(self):
        """
        ▶ Click [Create exercise button]

        - ✔ Button - visible
        - ▶ Button - click
        """
        self.check_create_exercise_btn()
        self.create_exercise_btn.click()

    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # [Toolbar]
    # ──────────────────────────────────┐
    def check_toolbar(self):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Create exercise button - visible

        """
        self.check_title()
        self.check_create_exercise_btn()
    # ──────────────────────────────────┘


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
        ✔ Check [Title] visible

        - ✔ Title - visible
        """
        error = f'❌ Create course page > Exercises > Toolbar > [Title] - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check [Title] text

        - ✔ Text - correct
        """
        error = f'❌ Create course page > Exercises > Toolbar > [Title] - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # [Create exercise button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_create_exercise_btn(self):
        """
        ✔ Check [Create exercise button]

        - ✔ Button - visible
        """
        self.check_create_exercise_btn_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_create_exercise_btn_visible(self):
        """
        ✔ Check [Create exercise button] visible

        .
        """
        error = f'❌ Create course page > Exercises > Toolbar > [Create exercise button] - invisible!'
        expect(self.create_exercise_btn, error).to_be_visible()


#=======================================================================================================================
