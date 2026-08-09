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
    def fill_registration_form(self, email: str, username: str, password: str):
        """
        Fill <Registration Form> fields of the Registration page

        - ▶ <Email field> - Fill
        - ▶ <Username field> - Fill
        - ▶ <Password field> - Fill
        - ✔ <Registration Form> fields - filled correctly

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.email_field.fill(email)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.check_registration_form_filled_correctly(email=email, username=username, password=password)


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


    # Registration Form (filled):
    # ───────────────────────────────────────────────────────┐
    def check_registration_form_filled_correctly(self, email: str, username: str, password: str):
        """
        Check <Registration form> fields of the Registration page - filled correctly (3-in-1)

        - ✔ <Email field> - filled correctly
        - ✔ <Username field> - filled correctly
        - ✔ <Password field> - filled correctly

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.check_email_field_filled_correctly(email)
        self.check_username_field_filled_correctly(username)
        self.check_password_field_filled_correctly(password)
    # ───────────────────────────────────────────────────────┘
    def check_email_field_filled_correctly(self, email: str):
        """
        Check <Email field> of the Registration form - filled correctly

        - ✔ <Email field> - filled correctly
        """
        error = '❌ <Email field> of the Registration form - filled incorrectly!'
        expect(self.email_field, error).to_have_value(email)

    def check_username_field_filled_correctly(self, username: str):
        """
        Check <Username field> of the Registration form - filled correctly

        - ✔ <Username field> - filled correctly
        """
        error = '❌ <Username field> of the Registration form - filled incorrectly!'
        expect(self.username_field, error).to_have_value(username)

    def check_password_field_filled_correctly(self, password: str):
        """
        Check <Password field> of the Registration form - filled correctly

        - ✔ <Password field> - filled correctly
        """
        error = '❌ <Password field> of the Registration form - filled incorrectly!'
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
