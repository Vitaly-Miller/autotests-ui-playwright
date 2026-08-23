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
        # [Email field]
        self.EMAIL_FIELD_NAME = 'Email'
        # [Password field]
        self.PASSWORD_FIELD_NAME = 'Password'

        # --------------------------------------- >>> [Element] path (for debug) ---------------------------------------
        # [Form]
        self.form_component = '❌ Login page > Form'
        # [Email field]
        self.email_field_element = f'{self.form_component} > [Email field]'
        # [Password field]
        self.password_field_element = f'{self.form_component} > [Password field]'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.email_field = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_field = page.get_by_test_id('login-form-password-input').locator('input')

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
        self.email_field.fill(email)
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
        self.password_field.fill(password)
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
                '✔ Check [Login form] field values'
                if all(param is not None for param in (email, password))
                else '✔ Check [Login form] UI'
        ):
            self.check_email_field(email)
            self.check_password_field(password)
    # ─────────────────────────────────────────┘

    # [Email field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
            with allure.step('✔ Check [Email field] value'):
                self.check_email_field_value(email)
        else:
            with allure.step('✔ Check [Email field] UI'):
                self.check_email_field_visible()
                self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Email field] visible')
    def check_email_field_visible(self):
        """
        ✔ Check [Email field] visible

        .
        """
        error = f'❌ Login page > Form > [Email field] - invisible!'
        expect(self.email_field, error).to_be_visible()

    @allure.step('✔ Check [Email field] name')
    def check_email_field_name(self):
        """
        ✔ Check [Email field] name

        .
        """
        error = f'❌ Login page > Form > [Email field] - incorrect name!'
        expect(self.email_field, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    @allure.step('✔ Check [Email field] value')
    def check_email_field_value(self, email: str):
        """
        ✔ Check [Email field] value

        :param email: Email
        """
        error = f'❌ Login page > Form > [Email field] - incorrect value!'
        expect(self.email_field, error).to_have_value(email)


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
            with allure.step('✔ Check [Password field] value'):
                self.check_password_field_value(password)
        else:
            with allure.step('✔ Check [Password field] UI'):
                self.check_password_field_visible()
                self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Password field] visible')
    def check_password_field_visible(self):
        """
        ✔ Check [Password field] visible

        .
        """
        error = f'❌ Login page > Form > [Password field] - invisible!'
        expect(self.password_field, error).to_be_visible()

    @allure.step('✔ Check [Password field] name')
    def check_password_field_name(self):
        """
        ✔ Check [Password field] name

        .
        """
        error = f'❌ Login page > Form > [Password field] - incorrect name!'
        expect(self.password_field, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    @allure.step('✔ Check [Password field] value')
    def check_password_field_value(self, password: str):
        """
        ✔ Check [Password field] value

        :param password: Password
        """
        error = f'❌ Login page > Form > [Password field] - incorrect value!'
        expect(self.password_field, error).to_have_value(password)


#=======================================================================================================================
