"""
Login page
"""
from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class LoginPage(BasePage):              # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ┌╴ 𝌆 DATA:
        # ├ Page
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'


        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('authentication-ui-course-title-text')
        # ├ Form fields
        self.email_field = page.get_by_label('Email')
        self.password_field = page.get_by_label('Password')
        # ├ Buttons/Links
        self.login_btn = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        # ├ Alerts
        self.wrong_email_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def fill_login_form(self, email: str, password: str):
        """
        - ▶ <Email> field - Fill
        - ▶ <Password> field - Fill
        - ✔ <Email> field  - filled correctly
        - ✔ <Password> field - filled correctly

        :param email: Email
        :param password: Password
        """
        self.email_field.fill(email)
        self.password_field.fill(password)
        expect(self.email_field).to_have_value(email)
        expect(self.password_field).to_have_value(password)


    def click_login_btn(self):
        """
        - ✔ <Login> button - enabled
        - ▶ <Login> button - Click
        """
        expect(self.login_btn).to_be_enabled()
        self.login_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar:
    def check_toolbar_title(self):
        """
        Check Toolbar title of the Login page

        - ✔ Header - visible
        - ✔ Header text - correct
        """
        error_visible = '❌ Toolbar title of the Login page - invisible!'
        error_text = '❌ Toolbar title text of the Login page - incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text('UI Course')


    # Buttons/Links:
    def check_registration_link(self, redirect_endpoint: str | None = None):
        """
        Check <Registration> link of the Login page

        - ✔ Link - enable
        - ✔ Link endpoint - correct
        """
        registration_page_endpoint = '#/auth/registration'
        redirect_endpoint = redirect_endpoint if redirect_endpoint else registration_page_endpoint  # Если <redirect_endpoint> не передан
        error_enabled = '❌ <Registration> link of the Login page is disabled!'
        error_url = '❌ <Registration> link of the Login page has incorrect endpoint!'
        expect(self.registration_link, error_enabled).to_be_enabled()
        expect(self.registration_link, error_url).to_have_attribute('href', redirect_endpoint)


    # Alerts:
    def check_wrong_email_or_password_alert(self):
        """
        Check <Wrong Email or Password> alert

        - Alert - visible
        - Alert text - correct
        """
        error_visible = '❌ <Wrong Email or Password> alert did not appear!'
        error_text = '❌ Incorrect <Wrong Email or Password> alert text!'
        expect(self.wrong_email_password_alert, error_visible).to_be_visible()
        expect(self.wrong_email_password_alert, error_text).to_have_text('Wrong email or password')

#=======================================================================================================================
