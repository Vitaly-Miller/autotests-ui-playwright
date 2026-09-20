"""
Dashboard page toolbar (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.text import Text

#=======================================================================================================================
class DashboardToolbarComponent(BaseComponent):
    """
    Dashboard page toolbar (component)

    - Title
    """
    PATH = 'Dashboard page > Toolbar'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('dashboard-toolbar-title-text')


    # -------------------------------------------------- ◈ ELEMENTS ----------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.PATH, 'Title')


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Toolbar]
    # ───────────────────────────────┐
    @allure.step('✔ Check [Toolbar]')
    def check(self):
        """
        ✔ Check [Toolbar]

        - ✔ Title
        """
        self.check_title()
    # ───────────────────────────────┘

    # [Title]
    @allure.step('✔ Check [Title]')
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.title().check_visible()
        self.title().check_text('Dashboard')


#=======================================================================================================================
