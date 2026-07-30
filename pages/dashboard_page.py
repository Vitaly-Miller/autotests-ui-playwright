"""
Dashboard page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, Locator, expect

#=======================================================================================================================
class DashboardPage(BasePage):          # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # 𝌆 DATA:
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        self.header_text = 'Dashboard'
        self.navbar_header_text = 'UI Course'
        self.navbar_welcome_title_text = 'Welcome, '  # static part


        # ㉧ LOCATORS (static):
        self.header = page.get_by_role(role='heading', name='Dashboard')
        self.navbar_header = page.get_by_test_id('navigation-navbar-app-title-text')


    # ㉧ LOCATORS {dynamic}:
    def navbar_welcome_title(self, username) -> Locator:
        return self.page.get_by_text(text=f'Welcome, {username}!')


    # ▶ ACTIONS:



    # ✔️EXPECTATIONS:
    def check_header_text(self):
        """
        Check Header text on the Dashboard page

        .
        """
        error = '❌ Header text on the Dashboard page is incorrect!'
        expect(self.header, error).to_have_text(self.header_text)


    def check_navbar_header_text(self):
        """
        Check Navbar header text on the Dashboard page

        .
        """
        error = '❌ Navbar header text on the Dashboard page is incorrect!'
        expect(self.navbar_header, error).to_have_text(self.navbar_header_text)


    def check_navbar_welcome_title_text(self, username):
        """
        Check Navbar welcome title text on the Dashboard page

        .
        """
        error = '❌ Navbar welcome title text on the Dashboard page is incorrect'
        expect(self.navbar_welcome_title(username), error).to_have_text(f'{self.navbar_welcome_title_text}{username}!')  # ex: Welcome, John!



#=======================================================================================================================
