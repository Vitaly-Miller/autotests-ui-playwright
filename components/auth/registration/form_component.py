"""
Registration page > [Form]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator
from elements.input_field import InputField

#=======================================================================================================================
class RegistrationFormComponent(BaseComponent):
    """
    [Form] component

    - Email input field
    - Username input field
    - Password input field
    """
    path = 'Registration page > Form'

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def email_field_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-form-email-input').locator('input')

    def username_field_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-form-username-input').locator('input')

    def password_field_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-form-password-input').locator('input')

    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def email_field(self) -> InputField:
        return InputField(self.email_field_locator(), self.path, 'Email field')

    def username_field(self) -> InputField:
        return InputField(self.username_field_locator(), self.path, 'Username field')

    def password_field(self) -> InputField:
        return InputField(self.password_field_locator(), self.path, 'Password field')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Registration form]
    # ────────────────────────────────────┐
    @allure.step('▶ Fill [Registration form]')
    def fill(self, email: str, username: str, password: str):
        """
        ▶ Fill [Registration form]

        - Email field - ▶ fill | ✔ value
        - Username field - ▶ fill | ✔ value
        - Password field - ▶ fill | ✔ value

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.fill_email_field(email)
        self.fill_username_field(username)
        self.fill_password_field(password)
    # ────────────────────────────────────┘
    # Fill [Email field]
    def fill_email_field(self, email: str):
        """
        ▶ Fill [Email field]

        :param email: Email
        """
        self.email_field().fill(email)

    # Fill [Username field]
    def fill_username_field(self, username: str):
        """
        ▶ Fill [Username field]

        :param username: Username
        """
        self.username_field().fill(username)

    # Fill [Password field]
    def fill_password_field(self, password: str):
        """
        ▶ Fill [Password field]

        :param password: Password
        """
        self.password_field().fill(password)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Registration Form]
    # ─────────────────────────────────────┐
    @allure.step('✔ Check [Registration form]')
    def check(
        self,
        email: str | None = None,
        username: str | None = None,
        password: str | None = None
    ):
        """
        ✔ Check [Registration form]

        - ✔ Email field - value / UI
        - ✔ Username field - value / UI
        - ✔ Password field - value / UI

        :param email: Email (optional)
        :param username: Username (optional)
        :param password: Password (optional)
        """
        self.check_email_field(email)
        self.check_username_field(username)
        self.check_password_field(password)
    # ─────────────────────────────────────┘

    # [Email field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Email field]')
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
            self.check_email_field_visible()
            self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_email_field_visible(self):
        """
        ✔ Check [Email field] is visible

        .
        """
        self.email_field().check_visible()

    # Name
    def check_email_field_name(self):
        """
        ✔ Check [Email field] name

        .
        """
        self.email_field().check_name(name='Email')

    # Value
    def check_email_field_value(self, email: str):
        """
        ✔ Check [Email field] value

        :param email: Email
        """
        self.email_field().check_value(value=email)


    # [Username field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Username field]')
    def check_username_field(self, username: str | None = None):
        """
        ✔ Check [Username field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name

        :param username: Username (optional)
        """
        if username is not None:
            self.check_username_field_value(username)
        else:
            self.check_username_field_visible()
            self.check_username_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_username_field_visible(self):
        """
        ✔ Check [Username field] is visible

        .
        """
        self.username_field().check_visible()

    # Name
    def check_username_field_name(self):
        """
        ✔ Check [Username field] name

        .
        """
        self.username_field().check_name(name='Username')

    # Value
    def check_username_field_value(self, username: str):
        """
        ✔ Check [Username field] value

        :param username: Username
        """
        self.username_field().check_value(value=username)


    # [Password field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Password field]')
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
            self.check_password_field_visible()
            self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_password_field_visible(self):
        """
        ✔ Check [Password field] is visible

        .
        """
        self.password_field().check_visible()

    # Name
    def check_password_field_name(self):
        """
        ✔ Check [Password field] name

        .
        """
        self.password_field().check_name(name='Password')

    # Value
    def check_password_field_value(self, password: str):
        """
        ✔ Check [Password field] value

        :param password: Password
        """
        self.password_field().check_value(value=password)


#=======================================================================================================================
