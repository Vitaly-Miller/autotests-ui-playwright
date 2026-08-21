"""
Create course page > Exercises > [Exercise] (component)
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar.sidebar_component import SidebarComponent
from components.navigation.navbar.navbar_component import NavbarComponent
from components.courses.create_course.exercise_toolbar_component import CreateCourseExerciseToolbarComponent
from components.courses.create_course.exercise_form_component import CreateCourseExerciseFormComponent

#=======================================================================================================================
"""
[Exercise]:
- Toolbar (component)
  - Title
  - Delete exercise button

- Form (component)
  - Title field
  - Description field
"""
class CreateCourseExerciseComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

    # ------------------------------------------------- ⿳ COMPONENTS --------------------------------------------------
        # <Bars>
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CreateCourseExerciseToolbarComponent(page)
        # <Form>
        self.form = CreateCourseExerciseFormComponent(page)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Exercise]
    # ───────────────────────────────────────┐
    def check_exercise(
            self,
            index: int,
            title: str | None = None,
            description: str | None = None
    ):
        """
        ✔ Check [Exercise]

        - ✔ Toolbar - Title | Delete exercise button
        - ✔ Form - Title | Description

        :param index: index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title
        :param description: Description
        :return:
        """
        self.toolbar.check(index)
        self.form.check(
            index=index,
            title=title,
            description=description)
    # ───────────────────────────────────────┘


#=======================================================================================================================
