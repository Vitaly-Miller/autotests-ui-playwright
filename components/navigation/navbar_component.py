"""
Navbar Component
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

        # ------------------------------------------- ㉧ LOCATORS (static) ----------------------------------------------
        self.title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ──────────────────────────────────────────┐
    def check_navbar(self, username: str):
        """
        Check <Navbar>

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ Welcome title - visible
        - ✔ Welcome title text - correct

        :param username: Username
        """
        self.check_title_visible()
        self.check_title_text()
        self.check_welcome_title_visible()
        self.check_welcome_title_text(username)
    # ──────────────────────────────────────────┘
    def check_title_visible(self):
        """
        Check <Navbar [Title]> - visible

        - ✔ Title - visible
        """
        error = f'❌ <Navbar [Title]> - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        Check <Navbar [Title] text> - correct

        - ✔ Text - correct
        """
        error = f'❌ <Navbar [Title] text> - incorrect!'
        expect(self.title, error).to_have_text('UI Course')

    def check_welcome_title_visible(self):
        """
        Check <Navbar [Welcome title]> - visible

        - ✔ Title - visible
        """
        error = f'❌ <Navbar [Welcome title]> - invisible!'
        expect(self.welcome_title, error).to_be_visible()

    def check_welcome_title_text(self, username):
        """
        Check <Navbar [Welcome title] text> - correct

        - ✔ Text - correct

        :param username: Username
        """
        error = f'❌ <Navbar [Welcome title] text> - incorrect!'
        expect(self.welcome_title, error).to_have_text(f'Welcome, {username}!')

#=======================================================================================================================
