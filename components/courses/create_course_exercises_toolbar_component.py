"""
Create course [Exercises] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page, expect

#=======================================================================================================================
"""
- Toolbar
  - [Title]
  - [Create exercise button]
"""
class CreateCourseExercisesComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------

        # ---------------------------------------------- ㉤ LOCATORS ----------------------------------------------------

        # -------------------------------------------- ✔️EXPECTATIONS --------------------------------------------------




#=======================================================================================================================
