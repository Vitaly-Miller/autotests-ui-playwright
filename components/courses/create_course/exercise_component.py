"""
Create course page > Exercises > [Exercise]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.courses.create_course.exercise_toolbar_component import CreateCourseExerciseToolbarComponent
from components.courses.create_course.exercise_form_component import CreateCourseExerciseFormComponent

#=======================================================================================================================

class CreateCourseExerciseComponent(BaseComponent):
    """
    [Exercise] component

    - Toolbar (component)
      - Title
      - Delete exercise button

    - Form (component)
      - Title field
      - Description field
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
        title: str | None = None,
        description: str | None = None
    ):
        """
        ✔ Check [Exercise]

        - ✔ Toolbar - Title | Delete exercise button
        - ✔ Form - Title | Description

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title (optional)
        :param description: Description (optional)
        """
        self.toolbar.check(index)
        self.form.check(
            index=index,
            title=title,
            description=description)
    # ────────────────────────────────┘

#=======================================================================================================================
