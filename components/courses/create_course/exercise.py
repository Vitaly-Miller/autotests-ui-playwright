"""
Create course page > Exercises > [Exercise]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.courses.create_course.exercise_toolbar import CreateCourseExerciseToolbarComponent
from components.courses.create_course.exercise_form import CreateCourseExerciseFormComponent

#=======================================================================================================================

class CreateCourseExerciseComponent(BaseComponent):
    """
    [Exercise] component

    - Toolbar (component)
      - Title
      - Delete exercise button

    - Form (component)
      - Title input field
      - Description input field
    """
    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        self.toolbar = CreateCourseExerciseToolbarComponent(page)
        self.form = CreateCourseExerciseFormComponent(page)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Exercise]
    # ────────────────────────────────┐
    @allure.step('✔ Check [Exercise]')
    def check(
        self,
        index: int,
        title: str = 'Exercise title',
        description: str = 'Exercise description'
    ):
        """
        ✔ Check [Exercise]

        - ✔ Toolbar - Title | Delete exercise button
        - ✔ Form - Title | Description

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title (Default: 'Exercise title')
        :param description: Description (Default: 'Exercise description')
        """
        self.toolbar.check(index)
        self.form.check(
            index=index,
            title=title,
            description=description)
    # ────────────────────────────────┘

#=======================================================================================================================
