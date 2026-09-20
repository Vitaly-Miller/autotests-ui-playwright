"""
Login form (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.input_field import InputField

#=======================================================================================================================
class LoginFormComponent(BaseComponent):
    """
    Login form (component)

    - Email input field
    - Password input field
    """
    PATH = 'Login page > Form'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def email_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('login-form-email-input').locator('input')

    def password_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('login-form-password-input').locator('input')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def email_input_field(self) -> InputField:
        return InputField(self.email_input_field_locator(), self.PATH, 'Email input field')

    def password_input_field(self) -> InputField:
        return InputField(self.password_input_field_locator(), self.PATH, 'Password input field')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Login form]
    @allure.step('▶ Fill [Login form]')
    def fill(self, email: str, password: str):
        """
        ▶ Fill [Login form]

        - Email input field - ▶ fill | ✔ value
        - Password input field - ▶ fill | ✔ value

        :param email: Email
        :param password: Password
        """
        self.email_input_field().fill(email)
        self.password_input_field().fill(password)


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Login Form]
    # ───────────────────────────────────────────┐
    @allure.step('✔ Check [Login form]')
    def check(self, email: str = '', password: str = ''):
        """
        ✔ Check [Login form]

        - ✔ Email input field
        - ✔ Password input field

        :param email: Email (Empty by default)
        :param password: Password (Empty by default)
        """
        self.check_email_input_field(email)
        self.check_password_input_field(password)
    # ───────────────────────────────────────────┘

    # [Email input field]
    @allure.step('✔ Check [Email input field]')
    def check_email_input_field(self, email: str = ''):
        """
        ✔ Check [Email input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - value (Empty by default)

        :param email: Email (optional)
        """
        self.email_input_field().check_visible()
        self.email_input_field().check_name(name='Email')
        self.email_input_field().check_value(email)

    # [Password input field]
    @allure.step('✔ Check [Password input field]')
    def check_password_input_field(self, password: str = ''):
        """
        ✔ Check [Password input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - value (Empty by default)

        :param password: Password (optional)
        """
        self.password_input_field().check_visible()
        self.password_input_field().check_name(name='Password')
        self.password_input_field().check_value(password)

#=======================================================================================================================
