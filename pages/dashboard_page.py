"""
Dashboard page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, Locator, expect

#=======================================================================================================================
dashboard_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

class DashboardPage(BasePage):          # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        #------------------------------------------ ㉧ LOCATORS (static) ------------------------------------------------
        self.header = page.get_by_role(role='heading', name='Dashboard')
        self.navbar_header = page.get_by_test_id('navigation-navbar-app-title-text')
        self.navbar_welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    #---------------------------------------------- ㉧ LOCATORS (dynamic) -----------------------------------------------
    # def user(self, name) -> Locator:
    #     return self.page.get_by_label(f'User-{name}')

    #------------------------------------------------ ▶ ACTIONS --------------------------------------------------------


    #------------------------------------------------ ✔️EXPECTATIONS ---------------------------------------------------
    # Dashboard header text
    def check_header_text(self):
        expect(self.header,
               '❌ Wrong Dashboard header text').to_have_text('Dashboard')

    # Dashboard navbar header text
    def check_navbar_header_text(self):
        expect(self.navbar_header,
               '❌ Wrong Navbar header text').to_have_text('UI Course')

    # Dashboard navbar welcome text (contains - "Welcome, " ...)
    def check_navbar_welcome_title_text(self):
        expect(self.navbar_welcome_title,
               '❌ Wrong Check Navbar welcome text').to_contain_text('Welcome, ')


#=======================================================================================================================
