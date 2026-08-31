"""
Navbar
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.text import Text

#=======================================================================================================================
class NavbarComponent(BaseComponent):
    """
    [Navbar] component

    - Title
    - Welcome title
    """
    path = 'Navbar'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('navigation-navbar-app-title-text')

    def welcome_title_locator(self) -> Locator:
        return self.page.get_by_test_id('navigation-navbar-welcome-title-text')

    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.path, 'Title')

    def welcome_title(self) -> Text:
        return Text(self.welcome_title_locator(), self.path, 'Welcome title')

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Navbar]
    # ────────────────────────────────────┐
    @allure.step('✔ Check [Navbar]')
    def check(self, username: str):
        """
        ✔ Check [Navbar]

        - ✔ Title - visible | - text
        - ✔ Welcome title - visible | - text

        :param username: Username
        """
        self.check_title()
        self.check_welcome_title(username)
    # ────────────────────────────────────┘

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
    # Visible
    def check_title_visible(self):
        """
        ✔ Check [Title] is visible

        .
        """
        self.title().check_visible()

    # Text
    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        self.title().check_text('UI Course')


    # [Welcome title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Welcome title]')
    def check_welcome_title(self, username: str):
        """
        ✔ Check [Welcome title]

        - ✔ Title - visible
        - ✔ Title - text

        :param username: Username
        """
        self.check_welcome_title_visible()
        self.check_welcome_title_text(username)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_welcome_title_visible(self):
        """
        ✔ Check [Welcome title] is visible

        .
        """
        self.welcome_title().check_visible()

    # Text
    def check_welcome_title_text(self, username: str):
        """
        ✔ Check [Welcome title] text

        :param username: Username
        """
        self.welcome_title().check_text(f'Welcome, {username}!')

#=======================================================================================================================
