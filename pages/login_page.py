"""
Login page
"""

from pages.base_page import BasePage
from playwright.sync_api import Page, expect



#=======================================================================================================================
class LoginPage(BasePage):              # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.TITLE_TEXT = 'UI Course'
        self.EMAIL_FIELD_NAME = 'Email'
        self.PASSWORD_FIELD_NAME = 'Password'
        self.LOGIN_BTN_TEXT = 'Login'
        self.REGISTRATION_LINK_TEXT = 'Registration'
        self.REGISTRATION_LINK_URL = '#/auth/registration'
        self.ALERT_TEXT = 'Wrong email or password'

        # ------------------------------------------ ㉧ LOCATORS (static) -----------------------------------------------
        # Toolbar
        self.title = page.get_by_test_id('authentication-ui-course-title-text')

        # Login Form input fields
        self.email_field = page.get_by_label('Email')
        self.password_field = page.get_by_label('Password')

        # Buttons/Links
        self.login_btn = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')

        # Alerts
        self.wrong_email_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def fill_login_form(self, email: str, password: str):
        """
        Fill <Login form> fields of the Login page

        - ▶ <Email field> - Fill
        - ▶ <Password field> - Fill
        - ✔ <Login form> fields - filled correctly

        :param email: Email
        :param password: Password
        """
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.check_login_form(email=email, password=password)


    def click_login_btn(self):
        """
        Click <Login button> of the Login page

        - ✔ Button - enabled
        - ▶ Button - Click
        """
        self.check_login_btn()
        self.login_btn.click()


    def click_registration_link(self):
        """
        Click <Registration link> of the Login page

        - ✔ Link - visible | Text - correct | URL - correct
        - ▶ Link - Click
        """
        self.check_registration_link()
        self.registration_link.click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ALL Elements
    # ══════════════════════════════════════╗
    def check_all_elements(self):
        """
        Check ALL Elements of the Login page

        - ✔ Title
        - ✔ Login Form (unfilled)
        - ✔ Login button - disabled
        - ✔ Registration link
        """
        self.check_title()
        self.check_login_form()
        self.check_login_btn(enable=False)
        self.check_registration_link()
    # ══════════════════════════════════════╝

    # Title:
    # ───────────────────────────────────┐
    def check_title(self):
        """
        Check <Title> of the Registration page

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        self.check_title_visible()
        self.check_title_text()
    # ───────────────────────────────────┘
    def check_title_visible(self):
        """
        Check <Title> of the Login page - visible

        - ✔ Title - visible
        """
        error = '❌ <Title> of the Login page - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        Check <Title text> of the Login page - correct

        - ✔ Text - correct
        """
        error = '❌ <Title text> of the Login page - incorrect!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # Login Form:
    # ─────────────────────────────────────────────────────────────────────┐
    def check_login_form(
            self,
            email: str | None = None,
            password: str| None = None):
        """
        Check <Login form> fields of the Login page

        - ✔ Email field - visible | Name - correct | Filled - correctly (if is passed)
        - ✔ Password field - visible | Name - correct | Filled - correctly (if is passed)

        :param email: Email (optional)
        :param password: Password (optional)
        """
        self.check_email_field(email)
        self.check_password_field(password)
    # ─────────────────────────────────────────────────────────────────────┘

    # - Email field
    # ───────────────────────────────────────────────────────┐
    def check_email_field(self, email: str | None = None):
        """
        Check <Login form [Email field]> of the Login page

        - ✔ Field - visible
        - ✔ Field Name - correct
        - ✔ Field - filled correctly (if is passed)
        """
        if email:
            self.check_email_field_filled_correctly(email)
        else:
            self.check_email_field_visible()
            self.check_email_field_name()
    # ───────────────────────────────────────────────────────┘
    def check_email_field_visible(self):
        """
        Check <Login form [Email field]> of the Login page - visible

        - ✔ Field - visible
        """
        error = '❌ <Login form [Email field]> of the Login page - invisible!'
        expect(self.email_field, error).to_be_visible()

    def check_email_field_name(self):
        """
        Check <Login form [Email field Name]> of the Login page - correct

        - ✔ Field Name - correct
        """
        error = '❌ <Login form [Email field Name]> of the Login page - incorrect!'
        expect(self.email_field, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    def check_email_field_filled_correctly(self, email: str):
        """
        Check <Login form [Email field]> of the Login page - filled correctly

        - ✔ Field - filled correctly
        """
        error = '❌ <Login form [Email field]> of the Login page - filled incorrectly!'
        expect(self.email_field, error).to_have_value(email)

    # - Password field
    # ──────────────────────────────────────────────────────────┐
    def check_password_field(self, password: str | None = None):
        """
        Check <Registration form [Password field]> of the Registration page

        - ✔ Field - visible
        - ✔ Field Name - correct
        - ✔ Field - filled correctly (if is passed)
        """
        if password:
            self.check_password_field_filled_correctly(password)
        else:
            self.check_password_field_visible()
            self.check_password_field_name()
    # ──────────────────────────────────────────────────────────┘
    def check_password_field_visible(self):
        """
        Check <Login form [Password field]> of the Login page - visible

        - ✔ Field - visible
        """
        error = '❌ <Login form [Password field]> of the Login page - invisible!'
        expect(self.password_field, error).to_be_visible()

    def check_password_field_name(self):
        """
        Check <Login form [Password field Name]> of the Login page - correct

        - ✔ Field Name - correct
        """
        error = '❌ <Login form [Password field Name]> of the Login page - incorrect!'
        expect(self.password_field, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    def check_password_field_filled_correctly(self, password: str):
        """
        Check <Login form [Password field]> of the Login page - filled correctly

        - ✔ Field - filled correctly
        """
        error = '❌ <Login form [Password field]> of the Login page - filled incorrectly!'
        expect(self.password_field, error).to_have_value(password)


    # Login Button:
    # ─────────────────────────────────────────────┐
    def check_login_btn(self, enable: bool = True):
        """
        Check <Login button> of the Login page

        - ✔ Button - enabled / disabled
        - ✔ Button text - correct
        """
        if enable:
            self.check_login_btn_enable()
        else:
            self.check_login_btn_disabled()
        self.check_login_btn_text()
    # ─────────────────────────────────────────────┘
    def check_login_btn_enable(self):
        """
        Check <Login button> of the Login page - enabled

        - ✔ Button - enabled
        """
        error = '❌ <Login button> of the Login page - disabled!'
        expect(self.login_btn, error).to_be_enabled()

    def check_login_btn_disabled(self):
        """
        Check <Login button> of the Login page - disabled

        (Until the Login form is completed successfully)

        - ✔ Button - disabled
        """
        error = '❌ <Login button> of the Login page - enabled!'
        expect(self.login_btn, error).to_be_disabled()

    def check_login_btn_text(self):
        """
        Check <Login Button text> of the Login page - correct

        - ✔ Text - correct
        """
        error = '❌ <Login Button text> of the Login page - incorrect!'
        expect(self.login_btn, error).to_have_text(self.LOGIN_BTN_TEXT)


    # Registration Link:
    # ────────────────────────────────────────┐
    def check_registration_link(self):
        """
        Check <Registration link> of the Login page

        - ✔ Link - visible
        - ✔ Link text - correct
        - ✔ Link URL - correct
        """
        self.check_registration_link_visible()
        self.check_registration_link_text()
        self.check_registration_link_url()
    # ────────────────────────────────────────┘
    def check_registration_link_visible(self):
        """
        Check <Registration link> of the Login page - visible

        - ✔ Link - visible
        """
        error = '❌ <Registration link> of the Login page - invisible!'
        expect(self.registration_link, error).to_be_visible()

    def check_registration_link_text(self):
        """
        Check <Registration link text> of the Login page - correct

        - ✔ Text - correct
        """
        error = '❌ <Registration link text> of the Login page - incorrect!'
        expect(self.registration_link, error).to_have_text(self.REGISTRATION_LINK_TEXT)

    def check_registration_link_url(self):
        """
        Check <Registration link [URL]> on the Login page - correct

        - ✔ URL - correct
        """
        error = '❌ <Registration link [URL]> of the Login page - incorrect!'
        expect(self.registration_link, error).to_have_attribute('href', self.REGISTRATION_LINK_URL)


    # Alert:
    # ────────────────────────────────────────────────────┐
    def wrong_email_or_password_alert(self):
        """
        Check <Wrong Email or Password> alert of the Login page

        - ✔ Alert - visible
        - ✔ Alert text - correct
        """
        self.check_wrong_email_or_password_alert_visible()
        self.check_wrong_email_or_password_alert_text()
    # ────────────────────────────────────────────────────┘
    def check_wrong_email_or_password_alert_visible(self):
        """
        Check <Wrong Email or Password alert> - visible

        - ✔ Alert - visible
        """
        error = '❌ <Wrong Email or Password alert> - invisible!'
        expect(self.wrong_email_password_alert, error).to_be_visible()

    def check_wrong_email_or_password_alert_text(self):
        """
        Check <Wrong Email or Password alert> text - correct

        - ✔ Text - correct
        """
        error = '❌ <Wrong Email or Password alert text> - incorrect!'
        expect(self.wrong_email_password_alert, error).to_have_text(self.ALERT_TEXT)


#=======================================================================================================================
