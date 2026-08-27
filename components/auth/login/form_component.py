"""
Login page > [Form] (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


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
        # Fields names
        self.EMAIL_FIELD_NAME = 'Email'
        self.PASSWORD_FIELD_NAME = 'Password'

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.form_component = '❌ Login page > Form'
        self.email_field_element = f'{self.form_component} > [Email field]'
        self.password_field_element = f'{self.form_component} > [Password field]'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.email_field_locator = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_field_locator = page.get_by_test_id('login-form-password-input').locator('input')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Login form]
    # ────────────────────────────────────┐
    @allure.step('▶ Fill [Login form]')
    def fill(
            self,
            email: str,
            password: str
    ):
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
        self.email_field_locator.fill(email)
        self.check_email_field_value(email)

    # Fill [Password field]
    @allure.step('▶ Fill [Password field]')
    def fill_password_field(self, password: str):
        """
        ▶ Fill [Password field]

        - ▶ Field - fill
        - ✔ Field - value

        :param password: Password
        """
        self.password_field_locator.fill(password)
        self.check_password_field_value(password)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Form]
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
                '✔ Check values of [Login form] fields'
                if all(param is not None for param in (email, password))
                else '✔ Check UI of [Login form]'
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
            with allure.step('✔ Check value of [Email field]'):
                self.check_email_field_value(email)
        else:
            with allure.step('✔ Check UI of [Email field]'):
                self.check_email_field_visible()
                self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Email field]')
    def check_email_field_visible(self):
        """
        ✔ Check visible [Email field]

        .
        """
        error = f'{self.email_field_element} - invisible!'
        expect(self.email_field_locator, error).to_be_visible()

    @allure.step('✔ Check name of [Email field]')
    def check_email_field_name(self):
        """
        ✔ Check name of [Email field]

        .
        """
        error = f'{self.email_field_element} - incorrect name!'
        expect(self.email_field_locator, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    @allure.step('✔ Check value of [Email field]')
    def check_email_field_value(self, email: str):
        """
        ✔ Check value of [Email field]

        :param email: Email
        """
        error = f'{self.email_field_element} - incorrect value!'
        expect(self.email_field_locator, error).to_have_value(email)


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
            with allure.step('✔ Check value of [Password field]'):
                self.check_password_field_value(password)
        else:
            with allure.step('✔ Check UI of [Password field]'):
                self.check_password_field_visible()
                self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Password field]')
    def check_password_field_visible(self):
        """
        ✔ Check visible [Password field]

        .
        """
        error = f'{self.password_field_element} - invisible!'
        expect(self.password_field_locator, error).to_be_visible()

    @allure.step('✔ Check name of [Password field]')
    def check_password_field_name(self):
        """
        ✔ Check name of [Password field]

        .
        """
        error = f'{self.password_field_element} - incorrect name!'
        expect(self.password_field_locator, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    @allure.step('✔ Check value of [Password field]')
    def check_password_field_value(self, password: str):
        """
        ✔ Check value of [Password field]

        :param password: Password
        """
        error = f'{self.password_field_element} - incorrect value!'
        expect(self.password_field_locator, error).to_have_value(password)


#=======================================================================================================================
