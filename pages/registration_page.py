"""
Registration page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class RegistrationPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.TITLE_TEXT = 'UI Course'
        self.EMAIL_FIELD_NAME = 'Email'
        self.USERNAME_FIELD_NAME = 'Username'
        self.PASSWORD_FIELD_NAME = 'Password'
        self.REGISTRATION_BTN_TEXT = 'Registration'
        self.LOGIN_LINK_TEXT = 'Login'
        self.LOGIN_LINK_URL = '#/auth/login'

        # --------------------------------------------╴ ㉧ LOCATORS (static) --------------------------------------------
        # Title
        self.title = page.get_by_test_id('authentication-ui-course-title-text')

        # Registration Form fields
        self.email_field = page.get_by_role(role='textbox', name='Email')
        self.username_field = page.get_by_role(role='textbox', name='Username')
        self.password_field = page.get_by_role(role='textbox', name='Password')

        # Buttons/Links
        self.registration_btn = page.get_by_role(role='button', name='Registration')
        self.login_link = page.get_by_role(role='link', name='Login')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def fill_registration_form(
            self,
            email: str,
            username: str,
            password: str):
        """
        Fill <Registration Form> fields of the Registration page

        - ▶ Email field - Fill
        - ▶ Username field - Fill
        - ▶ Password field - Fill
        - ✔ <Registration Form> fields - filled correctly

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.email_field.fill(email)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.check_registration_form(
            email=email,
            username=username,
            password=password)

    def click_registration_btn(self):
        """
        Click <Registration> button of the Registration page

        - ✔ Button - enabled
        - ▶ Button - Click
        """
        self.check_registration_btn()
        self.registration_btn.click()


    def click_login_link(self):
        """
        Click <Login link> of the Registration page

        - ✔ Link - visible | Text - correct | URL - correct
        - ▶ Link - Click
        """
        self.check_login_link()
        self.login_link.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ALL Elements
    # ══════════════════════════════════════════════╗
    def check_all_elements(self):
        """
        Check ALL Elements of the Registration page

        - ✔ Title
        - ✔ Registration Form (unfilled)
        - ✔ Registration button - disabled
        - ✔ Login link
        """
        self.check_title()
        self.check_registration_form()
        self.check_registration_btn(enable=False)
        self.check_login_link()
    # ══════════════════════════════════════════════╝

    # Title:
    # ──────────────────────────────┐
    def check_title(self):
        """
        Check <Title> of the Registration page

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        self.check_title_visible()
        self.check_title_text()
    # ──────────────────────────────┘
    def check_title_visible(self):
        """
        Check <Title> of the Registration page - visible

        - ✔ Title - visible
        """
        error = '❌ <Title> of the Registration page - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        Check <Title text> of the Registration page - correct!

        - ✔ Text - correct
        """
        error = '❌ <Title text> of the Registration page - incorrect!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # Registration Form:
    # ───────────────────────────────────────────────────────┐
    def check_registration_form(
            self,
            email: str | None = None,
            username: str | None = None,
            password: str | None = None):
        """
        Check <Registration form> fields of the Registration page

        - ✔ Email field - visible | Name - correct | Filled - correctly (if is passed)
        - ✔ Username field - visible | Name - correct | Filled - correctly (if is passed)
        - ✔ Password field - visible | Name - correct | Filled - correctly (if is passed)

        :param email: Email (optional)
        :param username: Username (optional)
        :param password: Password (optional)
        """
        self.check_email_field(email)
        self.check_username_field(username)
        self.check_password_field(password)
    # ───────────────────────────────────────────────────────┘

    # Email field
    # ───────────────────────────────────────────────────────┐
    def check_email_field(self, email: str | None = None):
        """
        Check <Registration form [Email field]> of the Registration page

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
        Check <Registration form [Email field]> of the Registration page - visible

        - ✔ Field - visible
        """
        error = '❌ <Registration form [Email field]> of the Registration page - invisible!'
        expect(self.email_field, error).to_be_visible()

    def check_email_field_name(self):
        """
        Check <Registration form [Email field Name]> of the Registration page - correct

        - ✔ Field Name - correct
        """
        error = '❌ <Registration form [Email field Name]> of the Registration page - incorrect!'
        expect(self.email_field, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    def check_email_field_filled_correctly(self, email: str):
        """
        Check <Registration form [Email field]> of the Registration page - filled correctly

        - ✔ Field - filled correctly
        """
        error = '❌ <Registration form [Email field]> of the Registration page - filled incorrectly!'
        expect(self.email_field, error).to_have_value(email)

    # Username field
    # ───────────────────────────────────────────────────────┐
    def check_username_field(self, username: str | None = None):
        """
        Check <Registration form [Username field]> of the Registration page

        - ✔ Field - visible
        - ✔ Field Name - correct
        - ✔ Field - filled correctly (if is passed)
        """
        if username:
            self.check_username_field_filled_correctly(username)
        else:
            self.check_username_field_visible()
            self.check_username_field_name()
    # ───────────────────────────────────────────────────────┘
    def check_username_field_visible(self):
        """
        Check <Registration form [Username field]> of the Registration page - visible

        - ✔ Field - visible
        """
        error = '❌ <Registration form [Username field]> of the Registration page - invisible!'
        expect(self.username_field, error).to_be_visible()

    def check_username_field_name(self):
        """
        Check <Registration form [Username field Name]> of the Registration page - correct

        - ✔ Field Name - correct
        """
        error = '❌ <Registration form [Username field Name]> of the Registration page - incorrect!'
        expect(self.username_field, error).to_have_accessible_name(self.USERNAME_FIELD_NAME)

    def check_username_field_filled_correctly(self, username: str):
        """
        Check <Registration form [Username field] of the Registration page - filled correctly

        - ✔ Field - filled correctly
        """
        error = '❌ <Registration form [Username field] of the Registration page - filled incorrectly!'
        expect(self.username_field, error).to_have_value(username)

    # Password field
    # ───────────────────────────────────────────────────────┐
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
    # ───────────────────────────────────────────────────────┘
    def check_password_field_visible(self):
        """
        Check <Registration form [Password field]> of the Registration page - visible

        - ✔ Field - visible
        """
        error = '❌ <Registration form [Password field]> of the Registration page - invisible!'
        expect(self.password_field, error).to_be_visible()

    def check_password_field_name(self):
        """
        Check <Registration form [Password field Name]> of the Registration page - correct

        - ✔ Field Name - correct
        """
        error = '❌ <Registration form [Password field Name]> of the Registration page - incorrect!'
        expect(self.password_field, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    def check_password_field_filled_correctly(self, password: str):
        """
        Check <Registration form [Password field] of the Registration page - filled correctly

        - ✔ Field - filled correctly
        """
        error = '❌ <Registration form [Password field] of the Registration page - filled incorrectly!'
        expect(self.password_field, error).to_have_value(password)



    # Registration Button:
    # ────────────────────────────────────────────────────┐
    def check_registration_btn(self, enable: bool = True):
        """
        Check <Registration button> of the Registration page

        - ✔ Button - enabled / disabled
        - ✔ Button text - correct
        """
        if enable:
            self.check_registration_btn_enable()
        else:
            self.check_registration_btn_disable()
        self.check_registration_btn_text()
    # ────────────────────────────────────────────────────┘
    def check_registration_btn_enable(self):
        """
        Check <Registration button> of the Registration page - enabled!

        - ✔ Button - enabled
        """
        error = '❌ <Registration button> of the Registration page - disabled!'
        expect(self.registration_btn, error).to_be_enabled()

    def check_registration_btn_disable(self):
        """
        Check <Registration button> of the Registration page - disabled!

        (Until the Registration form is completed successfully)

        - ✔ Button - disabled
        """
        error = '❌ <Registration button> of the Registration page - enabled!'
        expect(self.registration_btn, error).to_be_disabled()

    def check_registration_btn_text(self):
        """
        Check <Registration button text> of the Registration page - correct

        - ✔ Button text - correct
        """
        error = '❌ <Registration button text> of the Registration page - incorrect!'
        expect(self.registration_btn, error).to_have_text(self.REGISTRATION_BTN_TEXT)


    # Login Link:
    # ───────────────────────────────────┐
    def check_login_link(self):
        """
        Check <Login> link of the Registration page

        - ✔ Link - visible
        - ✔ Link text - correct
        - ✔ Link URL - correct
        """
        self.check_login_link_visible()
        self.check_login_link_text()
        self.check_login_link_url()
    # ───────────────────────────────────┘
    def check_login_link_visible(self):
        """
        Check <Login link> of the Registration page - visible

        - ✔ Link - visible
        """
        error = '❌ <Login link> of the Registration page - invisible!'
        expect(self.login_link, error).to_be_visible()

    def check_login_link_text(self):
        """
        Check <Login link text> of the Registration page - correct

        - ✔ Link text - correct
        """
        error = '❌ <Login link text> of the Registration page - incorrect!'
        expect(self.login_link, error).to_have_text(self.LOGIN_LINK_TEXT)

    def check_login_link_url(self):
        """
        Check <Login link> URL on the Registration page - correct

        - ✔ Link URL - correct
        """
        error = '❌ <Login link> URL of the Registration page - incorrect!'
        expect(self.login_link, error).to_have_attribute('href', self.LOGIN_LINK_URL)

#=======================================================================================================================
