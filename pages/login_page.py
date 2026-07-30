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
        # ├ Toolbar
        self.toolbar_title_text = 'UI Course'
        # ├ Alerts
        self.wrong_email_password_alert_text = 'Wrong email or password'
        # ├ Buttons/Links
        self.login_btn_text = 'LOGIN'

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
        ▶ Actions:
        ----------
        - Fill Login form

        ✔ Expectations:
        ---------------
        - Login form fields filled correctly

        :param email: Email
        :param password: Password
        """
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.check_login_form_fields_filled(email=email, password=password)


    def click_login_btn(self):
        """
        ✔ Expectations (func):
        ---------------
        - Button is enabled
        - Button text is correct

        ▶ Actions:
        ----------
        - Click button

        """
        self.check_login_btn()
        self.login_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Form fields:
    def check_login_form_fields_filled(self, email: str, password: str):
        """
        Check Login form fields filled correctly

        - Email field - filled correctly
        - Password field - filled correctly

        :param email: Email
        :param password: Password
        """
        error_email = '❌ Email field did not fill!'
        error_password = '❌ Password field did not fill!'
        expect(self.email_field, error_email).to_have_value(email)
        expect(self.password_field, error_password).to_have_value(password)


    # Toolbar:
    def check_toolbar_title(self):
        """
        Check Toolbar title on the Login page

        - Header is visible
        - Header text is correct
        """
        error_visible = '❌ Toolbar title on the Login page is invisible!'
        error_text = '❌ Toolbar title text on the Login page is incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text(self.toolbar_title_text)


    # Buttons/Links:
    def check_login_btn(self):
        """
        Check <Login button>

        - Button is enabled
        - Button text is correct
        """
        error_enabled = '❌ Login button is disabled!'
        error_text = '❌ Login button text is incorrect!'
        expect(self.login_btn, error_enabled).to_be_enabled()
        expect(self.login_btn, error_text).to_have_text(self.login_btn_text)


    def check_registration_link(self, redirect_endpoint: str | None = None):
        """
        Check <Registration link> on the Login page

        - Link is enable
        - Link endpoint is correct
        """
        registration_page_endpoint = '#/auth/registration'
        redirect_endpoint = redirect_endpoint if redirect_endpoint else registration_page_endpoint  # Если <link_url> не передан
        error_enabled = '❌ <Registration link> on the Login page is disabled!'
        error_url = '❌ <Registration link> on the Login page has incorrect endpoint!'
        expect(self.registration_link, error_enabled).to_be_enabled()
        expect(self.registration_link, error_url).to_have_attribute('href', redirect_endpoint)


    # Alerts:
    def check_wrong_email_or_password_alert(self):
        """
        Check <Wrong Email or Password> alert

        - Alert is visible
        - Alert text is correct
        """
        error_visible = '❌ Alert did not appear!'
        error_text = '❌ Incorrect alert text!'
        expect(self.wrong_email_password_alert, error_visible).to_be_visible()
        expect(self.wrong_email_password_alert, error_text).to_have_text(self.wrong_email_password_alert_text)

#=======================================================================================================================
