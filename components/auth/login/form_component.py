"""
Login page > [Form]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.input_field import InputField

#=======================================================================================================================
"""
[Form]:
- Email field
- Password field
"""
class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.EMAIL_FIELD_NAME = 'Email'
        self.PASSWORD_FIELD_NAME = 'Password'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.email_field_locator = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_field_locator = page.get_by_test_id('login-form-password-input').locator('input')

        # ---------------------------------------------- ◈ ELEMENTS ----------------------------------------------------
        self.path = 'Login page > Form'

        self.email_field = InputField(self.email_field_locator, self.path, 'Email field')
        self.password_field = InputField(self.password_field_locator, self.path, 'Password field')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Login form]
    # ────────────────────────────────────┐
    @allure.step('▶ Fill [Login form]')
    def fill_login_form(self, email: str, password: str):
        """
        ▶ Fill [Login form]

        - Email field - ▶ fill | ✔ value
        - Password field - ▶ fill | ✔ value

        :param email: Email
        :param password: Password
        """
        self.fill_email_field(email)
        self.fill_password_field(password)
    # ────────────────────────────────────┘
    # Fill [Email field]
    @allure.step('▶ Fill [Email field]')
    def fill_email_field(self, email: str):
        """
        ▶ Fill [Email field]

        - ▶ Field - fill
        - ✔ Field - value

        :param email: Email
        """
        self.email_field.fill(email)
        self.check_email_field_value(email)

    # Fill [Password field]
    def fill_password_field(self, password: str):
        """
        ▶ Fill [Password field]

        - ▶ Field - fill
        - ✔ Field - value

        :param password: Password
        """
        self.password_field.fill(password)
        self.check_password_field_value(password)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Login Form]
    # ─────────────────────────────────────────┐
    def check_login_form(
            self,
            email: str | None = None,
            password: str | None = None
    ):
        """
        ✔ Check [Login form]

        If is passed:
        -------------
        - ✔ Email field - value
        - ✔ Password field - value

        If is NOT passed:
        ----------------
        - ✔ Email field - visible | - name
        - ✔ Password field - visible | - name

        :param email: Email (optional)
        :param password: Password (optional)
        """
        with allure.step(
                '✔ Check [Login form] fields values'
                if all(param is not None for param in (email, password))
                else '✔ Check [Login form] UI'
        ):
            self.check_email_field(email)
            self.check_password_field(password)
    # ─────────────────────────────────────────┘

    # [Email field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_email_field(self, email: str | None = None):
        """
        ✔ Check [Email field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name

        :param email: Email (optional)
        """
        if email is not None:
            self.check_email_field_value(email)
        else:
            with allure.step('✔ Check [Email field] UI'):
                self.check_email_field_visible()
                self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_email_field_visible(self):
        """
        ✔ Check [Email field] is visible

        .
        """
        self.email_field.check_visible()

    # Name
    def check_email_field_name(self):
        """
        ✔ Check [Email field] name

        .
        """
        self.email_field.check_name(name=self.EMAIL_FIELD_NAME)

    # Value
    def check_email_field_value(self, email: str):
        """
        ✔ Check [Email field] value

        :param email: Email
        """
        self.email_field.check_value(value=email)


    # [Password field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_password_field(self, password: str | None = None):
        """
        ✔ Check [Password field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name

        :param password: Password (optional)
        """
        if password is not None:
            self.check_password_field_value(password)
        else:
            with allure.step('✔ Check [Password field] UI'):
                self.check_password_field_visible()
                self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_password_field_visible(self):
        """
        ✔ Check [Password field] is visible

        .
        """
        self.password_field.check_visible()

    # Name
    def check_password_field_name(self):
        """
        ✔ Check [Password field] name

        .
        """
        self.password_field.check_name(name=self.PASSWORD_FIELD_NAME)

    # Value
    def check_password_field_value(self, password: str):
        """
        ✔ Check [Password field] value

        :param password: Password
        """
        self.password_field.check_value(value=password)


#=======================================================================================================================
