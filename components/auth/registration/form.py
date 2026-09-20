"""
Registration form (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.input_field import InputField

#=======================================================================================================================
class RegistrationFormComponent(BaseComponent):
    """
    Registration form (component)

    - Email input field
    - Username input field
    - Password input field
    """
    PATH = 'Registration page > Form'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def email_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-form-email-input').locator('input')

    def username_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-form-username-input').locator('input')

    def password_input_field_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-form-password-input').locator('input')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def email_input_field(self) -> InputField:
        return InputField(self.email_input_field_locator(), self.PATH, 'Email input field')

    def username_input_field(self) -> InputField:
        return InputField(self.username_input_field_locator(), self.PATH, 'Username input field')

    def password_input_field(self) -> InputField:
        return InputField(self.password_input_field_locator(), self.PATH, 'Password input field')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Registration form]
    @allure.step('▶ Fill [Registration form]')
    def fill(self, email: str, username: str, password: str):
        """
        ▶ Fill [Registration form]

        - Email input field - ▶ fill | ✔ value
        - Username input field - ▶ fill | ✔ value
        - Password input field - ▶ fill | ✔ value

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.email_input_field().fill(email)
        self.username_input_field().fill(username)
        self.password_input_field().fill(password)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Registration Form]
    # ───────────────────────────────────────────┐
    @allure.step('✔ Check [Registration form]')
    def check(self, email: str = '', username: str = '', password: str = ''):
        """
        ✔ Check [Registration form]

        - ✔ Email input field
        - ✔ Username input field
        - ✔ Password input field

        :param email: Email (Empty by default)
        :param username: Username (Empty by default)
        :param password: Password (Empty by default)
        """
        self.check_email_input_field(email)
        self.check_username_input_field(username)
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

    # [Username input field]
    @allure.step('✔ Check [Username input field]')
    def check_username_input_field(self, username: str = ''):
        """
        ✔ Check [Username input field]

        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - value (Empty by default)

        :param username: Username (optional)
        """
        self.username_input_field().check_visible()
        self.username_input_field().check_name(name='Username')
        self.username_input_field().check_value(username)

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
