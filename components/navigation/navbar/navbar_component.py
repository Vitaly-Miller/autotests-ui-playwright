"""
Navbar (component)
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
Elements:
- Title
- Welcome title
"""
class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # Titles
        self.TITLE_TEXT = 'UI Course'
        self.WELCOME_TITLE_TEXT = lambda username: f'Welcome, {username}!'

        # ------------------------------------------- ㉧ LOCATORS (static) ----------------------------------------------
        self.title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Navbar]
    # ────────────────────────────────────┐
    def check_navbar(self, username: str):
        """
        ✔ Check [Navbar]

        - ✔ Title - visible | - text
        - ✔ Welcome title - visible | - text

        :param username: Username
        """
        self.check_title()
        self.check_welcome_title(username)
    # ────────────────────────────────────┘


    # Navbar [Title]
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

        .
        """
        error = f'❌ Navbar > [Title] - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'❌ Navbar > [Title] - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # Navbar [Welcome title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_welcome_title(self, username):
        """
        ✔ Check [Welcome title]

        - ✔ Title - visible
        - ✔ Text - correct

        :param username: Username
        """
        self.check_welcome_title_visible()
        self.check_welcome_title_text(username)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_welcome_title_visible(self):
        """
        ✔ Check [Welcome title] visible

        .
        """
        error = f'❌ Navbar > [Welcome title] - invisible!'
        expect(self.welcome_title, error).to_be_visible()

    def check_welcome_title_text(self, username):
        """
        ✔ Check [Welcome title] text

        :param username: Username
        """
        error = f'❌ Navbar > [Welcome title] - incorrect text!'
        expect(self.welcome_title, error).to_have_text(self.WELCOME_TITLE_TEXT(username))

#=======================================================================================================================
