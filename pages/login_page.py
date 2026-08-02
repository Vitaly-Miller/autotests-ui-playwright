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
        Fill Login form of the Login page

        - ▶ <Email> field - Fill
        - ▶ <Password> field - Fill
        - ✔ <Email> field  - filled correctly
        - ✔ <Password> field - filled correctly

        :param email: Email
        :param password: Password
        """
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.check_login_form_filled_correctly(email=email, password=password)

    def click_login_btn_enabled(self):
        """
        Click <Login> button of the Login page - enabled

        .
        """
        self.check_login_btn_enable()
        self.login_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar:
    def check_toolbar_title_visible(self):
        """
        Check <Toolbar title> of the Login page - visible

        .
        """
        error = '❌ <Toolbar title> of the Login page - invisible!'
        expect(self.toolbar_title, error).to_be_visible()

    def check_toolbar_title_text(self, text: str = 'UI Course'):
        """
        Check <Toolbar title> text of the Login page - correct

        :param text: Login page text (default: "UI Course")
        """
        error = '❌ <Toolbar title> text of the Login page - incorrect!'
        expect(self.toolbar_title, error).to_have_text(text)


    # Form (filled):
    # ---------------- Check Suite ----------------
    def check_login_form_filled_correctly(self, email: str, password: str):
        """
        Check <Login form> - filled correctly.

        .
        """
        self.check_email_field_filled(email)
        self.check_password_field_filled(password)

    # ---------------------------------------------
    def check_email_field_filled(self, email: str):
        """
        Check <Email field> of the Login form - filled correctly

        .
        """
        error = '❌ <Email field> of the Login form - filled incorrect!'
        expect(self.email_field, error).to_have_value(email)

    def check_password_field_filled(self, password: str):
        """
        Check <Password field> of the Login form - filled correctly

        .
        """
        error = '❌ <Password field> of the Login form - filled incorrect!'
        expect(self.password_field, error).to_have_value(password)


    # Buttons:
    def check_login_btn_enable(self):
        """
        Check <Login button> of the Login page - enabled

        .
        """
        error = '❌ <Login button> of the Login page - disabled!'
        expect(self.login_btn, error).to_be_enabled()

    def check_login_btn_disabled(self):
        """
        Check <Login button> of the Login page - disabled

        .
        """
        error = '❌ <Login button> of the Login page - enabled!'
        expect(self.login_btn, error).to_be_disabled()

    def check_login_btn_text(self, text: str = 'Login'):
        """
        Check <Login button> text of the Login page - correct

        :param text: Login page text (default: "Login")
        """
        error = '❌ <Login button> text of the Login page - incorrect!'
        expect(self.login_btn, error).to_have_text(text)


    # Links:
    def check_registration_link_visible(self):
        """
        Check <Registration link> of the Login page - visible

        .
        """
        error = '❌ <Registration link> of the Login page - invisible!'
        expect(self.registration_link, error).to_be_visible()

    def check_registration_link_endpoint(self, endpoint: str = '#/auth/registration'):
        """
        Check <Registration link> endpoint on the Login page - correct

        :param endpoint: Registration page link endpoint (default: "#/auth/registration")
        """
        error = '❌ <Registration link> of the Login page has - incorrect endpoint!'
        expect(self.registration_link, error).to_have_attribute('href', endpoint)


    # Alerts:
    def check_wrong_email_or_password_alert_visible(self):
        """
        Check <Wrong Email or Password> alert - visible

        .
        """
        error = '❌ <Wrong Email or Password> alert did not appear/invisible!'
        expect(self.wrong_email_password_alert, error).to_be_visible()

    def check_wrong_email_or_password_alert_text(self):
        """
        Check <Wrong Email or Password> alert text

        - Alert - visible
        - Alert text - correct
        """
        error = '❌ <Wrong Email or Password> alert text - incorrect!'
        expect(self.wrong_email_password_alert, error).to_have_text('Wrong email or password')


#=======================================================================================================================
